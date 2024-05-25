from torch.utils.data import DataLoader
from torch import nn
from torch.optim import Adam
from torch.optim.lr_scheduler import CosineAnnealingLR
import torch.nn.functional as F

import torch
import numpy as np
import pandas as pd
import scipy.sparse as sp

import cv2
import math
import os
import gc
import types

from scipy.spatial import KDTree
from sklearn.decomposition import NMF
from sklearn.linear_model import LinearRegression
from sklearn.mixture import GaussianMixture

from .data import HE_Prediction_Dataset, HE_Dataset, HE_Score_Dataset, spatial_obj
from .model import DeepFuseNMFUnet, GraphAutoEncoder
from .utils import create_pseudo_spots, query_kdtree_parallel, construct_adjacency_matrix


class DeepFuseNMF_Runner:
    """
    The `DeepFuseNMF_Runner` class is a runner for the DeepFuseNMF model.

    Args:
        sections (dict): Dictionary containing the spatial objects for the sections.
        rank (int): The rank of the NMF model.
        results_path (str): The path to save the results.
        seed (int, optional): The seed for random number generation. Defaults to 123.
        verbose (bool, optional): Whether to print the progress or not. Defaults to False.

    Methods:
        get_NMF_score: Perform NMF and normalize the results.
        get_GCN_score: Get the smoothed GCN score for each section.
        get_VD_score: Get the VD score for each section.
        pretrain: Pretrain the DeepFuseNMF model based on the image prediction.
        train: Train the DeepFuseNMF model based on the image prediction and spot expression reconstruction.
        get_DeepFuseNMF_score: Get the pixel-wised DeepFuseNMF score for each section.

        _tissus_separation: Divide the tissue area into sub-tissue regions based on split size and redundancy ratio.
        _crate_pseudo_spots: Create pseudo spots for the tissue sections.
        _get_nearby_spots: Get the nearby spots based on the feasible domain, radius, and real spot coordinates.
        _find_nearby_spots: Find the nearby spots based on the spot coordinates and the feasible domain.
        _calculate_splits: Calculate the splits for either rows or columns.
        _get_image_embedding: Get the image embeddings based on the spot coordinates, radius, and image.
        _train_GCN: Train the GCN model to predict spots' GCN score (including pseudo spots).
        _prepare_pretrain: Prepare the pre-training process for the DeepFuseNMF model.
        _pretrain_model: Pre-train the DeepFuseNMF model based on the image prediction.
        _prepare_GCN: Prepare the training process for the GCN model.

    Example:
        >>> sections = {}
        >>> rank = 10
        >>> results_path = 'results'
        >>> seed = 123
        >>> verbose = False
        >>> runner = DeepFuseNMF_Runner(sections=sections, rank=rank, results_path=results_path, seed=seed, verbose=verbose)
        >>> runner.get_NMF_score()
    """

    def __init__(self,
                 sections: dict,
                 rank: int,
                 results_path: str,
                 seed: int = 123,
                 verbose: bool = False,
                 reference: list = None):

        self.sections = sections
        self.reference = reference
        self.num_genes = self.sections[list(self.sections.keys())[0]].spot_exp.shape[1]

        self.rank = rank
        self.results_path = results_path

        self.seed = seed
        self.verbose = verbose

        args_dict = {'num_channels': list(sections.values())[0].image.shape[0], 'split_size': 256, 'smooth_threshold': 0.01,
                     'redundant_ratio': 0.2, 'overlap_ratio': 0.15, 'bound_ratio': 0.05,

                     'num_workers': 4, 'batch_size': 32, 'lr_train': 4e-4, 'weight_decay': 1e-5, 'lda': 0.1,
                     'total_iter_pretrain': 5000, 'rec_iter': 200, 'eta_min': 1e-6,
                     'lr': 0.005, 'total_iter_gcn': 5000,
                     'total_iter_train': 2000, 'fix_iter_train': 1000}

        self.args = types.SimpleNamespace(**args_dict)
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        print(f'*** Using {self.device}... ***')

        self.GCN = None
        self.metagene = None

        self.model = DeepFuseNMFUnet(rank=self.rank, num_genes=self.num_genes, num_channels=self.args.num_channels,
                                     section_names=[section.section_name for section in self.sections.values()], reference=self.reference)
        self.model.to(self.device)

        self.train_loader = None

        # Get the tissue splits and create pseudo spots
        if self.verbose: print('*** Preparing the tissue splits and creating pseudo spots... ***')
        self._tissue_separation()
        self._crate_pseudo_spots()

    def _crate_pseudo_spots(self):
        # Create pseudo spots for the tissue sections.

        for _, section in self.sections.items():
            # Get the section details
            feasible_domain = section.feasible_domain
            radius = section.radius
            real_spot_coord = section.spot_coord
            num_pseudo_spots = min(round(real_spot_coord.shape[0] / 1000) * 5000, 100000)

            if self.verbose:
                print(f'*** Creating {num_pseudo_spots} pseudo spots for {section.section_name}... ***')

            # Get the image embeddings
            pseudo_spot_coord = create_pseudo_spots(feasible_domain=feasible_domain, radius=radius,
                                                    seed=self.seed, num_pseudo_spots=num_pseudo_spots)
            section.all_spot_coord = np.vstack((real_spot_coord, pseudo_spot_coord))

        # Get the nearby spots based on different settings
        self._get_nearby_spots(use_all_spot=False, use_section_range=False)
        self._get_nearby_spots(use_all_spot=True, use_section_range=False)
        self._get_nearby_spots(use_all_spot=True, use_section_range=True)

    def get_NMF_score(self,
                      save_score: bool = False):
        """
        Perform NMF and normalize the results.

        Args:
            save_score (bool, optional): Whether to save the score or not. Defaults to False.
        """

        # Prepare data
        spot_exp = np.vstack([self.sections[section].spot_exp for section in self.sections])

        # Perform NMF
        print('*** Performing NMF... ***')

        model_NMF = NMF(n_components=self.rank, init='nndsvd', random_state=self.seed, max_iter=2000)
        NMF_score = model_NMF.fit_transform(spot_exp)
        metagene = model_NMF.components_

        if self.reference is not None:
            self.model.gamma = self.model.gamma.to(self.device)

            # Before normalized, remove the batch effect
            start_i = 0
            for _, section in self.sections.items():
                end_i = start_i + section.num_spots
                section.scores['NMF_tmp'] = NMF_score[start_i:end_i]
                start_i = end_i

            for i, (_, section) in enumerate(self.sections.items()):
                if self.reference[i] is None:
                    section.scores['NMF'] = section.scores['NMF_tmp']
                    continue

                cur_score = section.scores['NMF_tmp']
                ref_score = self.sections[self.reference[i]].scores['NMF_tmp']

                beta = cur_score.mean(0) - ref_score.mean(0)
                cur_score = cur_score - np.matmul(np.ones(shape=(cur_score.shape[0], 1)),
                                                  np.resize(beta, (1, cur_score.shape[1])))

                cur_score[np.where(cur_score < 0)] = 0
                section.scores['NMF'] = cur_score

                self.model.gamma.data[i, :] = torch.tensor(np.matmul(beta.reshape(1, -1), metagene),
                                                           requires_grad=True).to(self.device)

            NMF_score = np.vstack([section.scores['NMF'] for section in self.sections.values()])
            for _, section in self.sections.items():
                section.scores.pop('NMF_tmp')

        # Normalize the results of NMF
        region_NMF_max = np.max(NMF_score, axis=0)
        NMF_score_normalized = NMF_score / region_NMF_max
        metagene_normalized = pd.DataFrame(metagene * region_NMF_max[:, np.newaxis])

        # Save the results
        metagene_normalized.to_csv(f'{self.results_path}/V_para_NMF.csv')
        self.metagene_NMF = metagene_normalized

        start_i = 0
        for _, section in self.sections.items():
            end_i = start_i + section.num_spots
            section.scores['NMF'] = NMF_score_normalized[start_i:end_i]
            start_i = end_i

            if save_score:
                os.makedirs(section.save_paths['NMF'], exist_ok=True)
                np.save(f'{section.save_paths["NMF"]}/NMF_score.npy', section.scores['NMF'])

    def _get_nearby_spots(self,
                          use_all_spot: bool = False,
                          use_section_range: bool = False):
        """
        Get the nearby spots based on the feasible domain, radius, and real spot coordinates.

        Args:
            use_all_spot (bool): Whether to use all spots or not.
            use_section_range (bool): Whether to use the section range or not.
        """

        for _, section in self.sections.items():
            # Get the section details
            feasible_domain = section.feasible_domain
            spot_coord = section.all_spot_coord if use_all_spot else section.spot_coord

            # Find the nearest spots
            if use_section_range:
                row_range, col_range = section.row_range, section.col_range
            else:
                row_range, col_range = feasible_domain.shape

            nearby_spots = self._find_nearby_spots(spot_coord=spot_coord, row_range=row_range, col_range=col_range)

            if use_section_range:
                section.vd_nearby_spots = nearby_spots
            else:
                if use_all_spot:
                    section.all_nearby_spots = nearby_spots
                else:
                    section.nearby_spots = nearby_spots

    def _find_nearby_spots(self,
                           spot_coord: np.ndarray,
                           row_range: tuple | int,
                           col_range: tuple | int) -> np.ndarray:
        """
        Find the nearby spots based on the spot coordinates and the feasible domain.

        Args:
            spot_coord (numpy.ndarray): Array containing spot coordinates.
            row_range (tuple | int): Tuple indicating the start and end row for the feasible domain.
            col_range (tuple | int): Tuple indicating the start and end column for the feasible domain.

        Returns:
            numpy.ndarray: Array of nearby spots.
        """

        # KDTree for nearest spot querying
        tree = KDTree(spot_coord)

        # Create grid for querying nearest spots
        if row_range.__class__ is not tuple:
            query_grid = np.vstack(
                (np.repeat(np.arange(row_range), col_range), np.tile(np.arange(col_range), row_range))).T
        else:
            query_grid = np.vstack((np.repeat(np.arange(row_range[0], row_range[1]), col_range[1] - col_range[0]),
                                    np.tile(np.arange(col_range[0], col_range[1]), row_range[1] - row_range[0]))).T

        return query_kdtree_parallel(tree, query_grid, workers=4)

    def _tissue_separation(self):
        # Divide the tissue area into sub-tissue regions based on split size and redundancy ratio.

        for name, section in self.sections.items():
            # Obtain the mask for the tissue area
            mask = section.mask_init

            # Obtain min and max values for row and column
            row_min, row_max = section.row_range
            col_min, col_max = section.col_range

            # Calculate row and column splits
            row_splits = self._calculate_splits(row_min, row_max)
            col_splits = self._calculate_splits(col_min, col_max)

            # Combine row and column splits to form sub-tissue coordinates
            tmp_tissue_coord = np.vstack((np.repeat(row_splits[:, 0], len(col_splits)),
                                          np.repeat(row_splits[:, 1], len(col_splits)),
                                          np.tile(col_splits[:, 0], len(row_splits)),
                                          np.tile(col_splits[:, 1], len(row_splits)))).T

            # Filter out sub-tissue coordinates with no tissue
            tissue_coord = []
            for tmp_coords in tmp_tissue_coord:
                sub_mask = mask[tmp_coords[0]:tmp_coords[1], tmp_coords[2]:tmp_coords[3]]
                if sub_mask.sum() > 255: tissue_coord.append(tmp_coords)

            section.tissue_coord = np.array(tissue_coord)

            if self.verbose:
                print(f'*** For section {name}, the tissue is divided into {len(tissue_coord)} sub-tissues ***')

    def _calculate_splits(self,
                          min_val: int,
                          max_val: int) -> np.ndarray:
        """
        Calculate the splits for either rows or columns.

        Args:
            min_val (int): The minimum value for the split.
            max_val (int): The maximum value for the split.

        Returns:
            numpy.ndarray: Array of split indices.
        """

        redundant_size = round(self.args.split_size * self.args.redundant_ratio)
        num_splits = int(np.ceil((max_val - min_val - redundant_size) / (self.args.split_size - redundant_size)))

        start_indices = np.arange(min_val, min_val + num_splits * (self.args.split_size - redundant_size),
                                  self.args.split_size - redundant_size)
        end_indices = start_indices + self.args.split_size
        if end_indices[-1] > max_val:
            end_indices[-1] = max_val
            start_indices[-1] = max_val - self.args.split_size

        return np.vstack((start_indices, end_indices)).T

    def pretrain(self, pretrain_path):
        """
        Pre-train the DeepFuseNMF model based on the image prediction.

        Args:
            pretrain_path (str): The path to save the pre-trained model.
        """

        self.model.training_mode = False

        if os.path.exists(pretrain_path):
            print(f'*** Load pre-trained model from {pretrain_path} ***')
            ckpt = torch.load(pretrain_path)
            for name in list(ckpt.keys()):
                if 'low_rank' in name or 'image_pred' in name:
                    ckpt.pop(name)

            self.model.load_state_dict(ckpt, strict=False)
        else:
            self._pretrain_model()
            print(f'*** Save pre-trained model to {pretrain_path} ***')
            torch.save(self.model.state_dict(), pretrain_path)

    def _prepare_pretrain(self):
        # Prepare the pre-training process for the DeepFuseNMF model

        self.model.train()
        for name, p in self.model.named_parameters():
            p.requires_grad = True

        # Prepare the training dataset
        self.train_dataset = torch.utils.data.ConcatDataset([
            HE_Prediction_Dataset(section=section, args=self.args) for name, section in self.sections.items()
        ])

        # Prepare the training loader
        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=self.args.batch_size, shuffle=True,
                                       drop_last=False, num_workers=self.args.num_workers)

        # Prepare the loss, optimizer and scheduler
        self.loss = nn.MSELoss()

        self.optimizer = Adam(self.model.parameters(), lr=self.args.lr_train, weight_decay=self.args.weight_decay)
        self.scheduler = CosineAnnealingLR(self.optimizer, T_max=self.args.total_iter_pretrain, eta_min=self.args.eta_min)

    def _pretrain_model(self):
        # Prepare the pre-training process

        self._prepare_pretrain()

        # Start the pre-training process
        last_loss, rec_loss = 1000., 0.

        epoch = current_iter = 0
        stop_flag = False
        while current_iter <= self.args.total_iter_pretrain:
            for img in self.train_loader:
                current_iter += 1
                img = img.to(self.device)
                out = self.model(img)

                loss = self.loss(out, img)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                self.scheduler.step()

                rec_loss += loss

                if current_iter % self.args.rec_iter == 0:
                    rec_loss = rec_loss.item() / self.args.rec_iter
                    if self.verbose:
                        print(f'[Iter: {current_iter} / {self.args.total_iter_pretrain}], Epoch: {epoch+1},'
                              f' Loss: {rec_loss:.6f}, Learning rate: {self.scheduler.get_last_lr()[0]:.6e}')

                    # Early stopping if the loss does not change much
                    if current_iter >= self.args.total_iter_pretrain // 2 and abs(1. - rec_loss / last_loss) < 0.05:
                        print("Reached convergence, stop early")
                        stop_flag = True
                        break

                    last_loss = rec_loss
                    rec_loss = 0.

            if stop_flag: break
            # end of iter
            epoch += 1

    def _get_image_embedding(self,
                             spot_coord: np.ndarray,
                             radius: int,
                             image: np.ndarray,
                             batch_size: int = 32,
                             embedding_size: int = 128) -> np.ndarray:
        """
        Get the image embeddings based on the spot coordinates, radius, and image.

        Args:
            spot_coord (numpy.ndarray): Array containing spot coordinates.
            radius (int): The radius within which to find coordinates.
            image (numpy.ndarray): sub-image.
            batch_size (int): The batch size for the image embeddings.
            embedding_size (int): The size of the image embeddings.

        Returns:
            numpy.ndarray: Array of image embeddings.
        """

        self.model.eval()

        # Extract sub-images and upsample to 256x256
        sub_images = nn.UpsamplingBilinear2d(size=256)(self._extract_image(spot_coord, radius, image))

        # Extract image embeddings
        image_embeddings = np.zeros((sub_images.shape[0], embedding_size))
        with torch.no_grad():
            for start_i in range(0, sub_images.shape[0], batch_size):
                end_i = min(start_i + batch_size, sub_images.shape[0])
                _, embeddings_batch = self.model(sub_images[start_i:end_i].to(self.device))
                image_embeddings[start_i:end_i] = torch.mean(embeddings_batch, dim=(2, 3)).cpu().numpy()

        return image_embeddings

    def _extract_image(self,
                       spot_coord: np.ndarray,
                       radius: int,
                       image: np.ndarray) -> torch.Tensor:
        """
        Extract the sub-image based on the spot coordinates, radius, and image.

        Args:
            spot_coord (numpy.ndarray): Array containing spot coordinates.
            radius (int): The radius within which to find coordinates.
            image (numpy.ndarray): Original image.

        Returns:
            torch.Tensor: The sub-image tensor.
        """

        img_size = radius * 2
        num_spots = spot_coord.shape[0]
        sub_images = np.zeros((num_spots, self.args.num_channels, 2 * img_size + 1, 2 * img_size + 1), dtype=np.float32)

        # Extract sub-image for each spot
        for spot_index in range(num_spots):
            center_row, center_col = round(spot_coord[spot_index, 0]), round(spot_coord[spot_index, 1])
            row_start, row_end = max(0, center_row - img_size + 1), min(image.shape[1] - 1, center_row + img_size + 1)
            col_start, col_end = max(0, center_col - img_size + 1), min(image.shape[2] - 1, center_col + img_size + 1)

            if row_start == 0: row_end = 2 * img_size
            if col_start == 0: col_end = 2 * img_size
            if row_end == image.shape[1] - 1: row_start = image.shape[1] - 1 - 2 * img_size
            if col_end == image.shape[2] - 1: col_start = image.shape[2] - 1 - 2 * img_size

            sub_images[spot_index, :, :, :] = image[:, row_start:row_end + 1, :][:, :, col_start:col_end + 1]

        return torch.tensor(sub_images)

    def _prepare_GCN(self,
                     adj_matrix: sp.csr_matrix,
                     num_spots: int):
        """
        Prepare the training process for the GCN model.

        Args:
            adj_matrix (numpy.ndarray): The adjacency matrix of the graph.
            num_spots (int): The number of spots in the dataset.
        """

        values = adj_matrix.data
        indices = np.vstack((adj_matrix.row, adj_matrix.col))
        i = torch.LongTensor(indices)
        v = torch.FloatTensor(values)
        shape = adj_matrix.shape

        adj_matrix = torch.sparse.FloatTensor(i, v, torch.Size(shape)).to(self.device)
        self.GCN = GraphAutoEncoder(adj_matrix=adj_matrix, num_spots=num_spots, rank=self.rank).to(self.device)
        self.GCN.train()

        # Prepare the loss, optimizer and scheduler
        self.loss = nn.MSELoss()
        self.optimizer = Adam(self.GCN.parameters(), lr=self.args.lr, weight_decay=self.args.weight_decay)
        self.scheduler = CosineAnnealingLR(self.optimizer, T_max=self.args.total_iter_gcn, eta_min=self.args.lr/4)

    def _train_GCN(self,
                   adj_matrix: sp.csr_matrix,
                   score: np.ndarray) -> np.ndarray:
        """
        Train the GCN model to predict spots' GCN score (including pseudo spots).

        Args:
            adj_matrix (numpy.ndarray): The adjacency matrix of the graph.
            score (numpy.ndarray): Array of spot scores.

        Returns:
            numpy.ndarray: Array of predicted spot scores.
        """

        score = torch.tensor(np.array(score), dtype=torch.float32, device=self.device)
        num_spots = score.shape[0]
        self._prepare_GCN(adj_matrix, num_spots)

        # Train the GCN model
        loss_cur = 0.
        for iter in range(self.args.total_iter_gcn):
            self.optimizer.zero_grad()

            pred = self.GCN(score)[:num_spots, :]
            loss = self.loss(pred, score)
            loss.backward()
            self.optimizer.step()
            self.scheduler.step()

            if self.verbose:
                loss_cur = loss_cur + loss.item()
                if (iter + 1) % self.args.rec_iter == 0:
                    print(f'[Iter: {iter + 1} / {self.args.total_iter_gcn}], Loss: {loss_cur / self.args.rec_iter:.6f}, '
                          f'Learning rate: {self.scheduler.get_last_lr()[0]:.6e}')
                    loss_cur = 0.

        # Get the predicted spot scores
        self.GCN.eval()
        with torch.no_grad():
            return self.GCN(score).cpu().detach().numpy()

    def get_GCN_score(self,
                      GMM_filter: bool = True,
                      save_score: bool = False):
        """
        Get the smoothed GCN score for each section.

        Args:
            GMM_filter (bool): Whether to filter low signal using Gaussian Mixture Model.
            save_score (bool): Whether to save the GCN score or not.
        """

        print('*** Performing GCN... ***')

        for _, section in self.sections.items():
            # Get the section details
            radius = section.radius
            image = section.image
            NMF_score = section.scores['NMF']

            # Get the image embeddings
            all_image_embeddings = self._get_image_embedding(section.all_spot_coord, radius, image)

            # Construct the adjacency matrix
            adjacency_matrix = construct_adjacency_matrix(spot_coord=section.all_spot_coord,
                                                          spot_embeddings=all_image_embeddings,
                                                          num_real_spots=NMF_score.shape[0])

            # Train the GCN
            if self.verbose: print(f'*** Training GCN for {section.section_name}... ***')
            gcn_score = self._train_GCN(adjacency_matrix, NMF_score)

            # Filter low signal using Gaussian Mixture Model
            if GMM_filter:
                for idx in range(self.rank):
                    data_use = gcn_score[:, idx].reshape(gcn_score.shape[0], 1)
                    gmm = GaussianMixture(2, covariance_type='full', random_state=self.seed).fit(data_use)
                    label_choose = np.argmax(gmm.means_)
                    labels = gmm.predict(data_use)
                    signal_remove_index = np.where(labels != label_choose)[0]
                    gcn_score[signal_remove_index, idx] = 0

            gcn_score[np.where(gcn_score < 0.1)] = 0
            section.scores['GCN'] = gcn_score

            if save_score:
                os.makedirs(section.save_paths['GCN'], exist_ok=True)
                np.save(f'{section.save_paths["GCN"]}/GCN.npy', gcn_score)

        # Delete the GCN model
        del self.GCN
        gc.collect()
        torch.cuda.empty_cache()

        # Refine the metagene
        LR = LinearRegression(fit_intercept=False, positive=True)
        all_score = np.vstack([section.scores['GCN'][:section.num_spots, :] for _, section in self.sections.items()])

        if self.reference is not None:
            all_exp = []
            for i, (_, section) in enumerate(self.sections.items()):
                if self.reference[i] is None:
                    all_exp.append(section.spot_exp)
                else:
                    all_exp.append(np.clip(section.spot_exp - self.model.gamma.data[i, :].cpu().numpy(), 0, None))
        else:
            all_exp = [section.spot_exp for _, section in self.sections.items()]

        all_exp = np.vstack(all_exp)
        LR_result = LR.fit(all_score, all_exp)
        self.metagene = LR_result.coef_.T

    def _smooth(self,
                spot_score: np.ndarray,
                kernel_size: int,
                threshold: float = 0.01) -> np.ndarray:
        """
        Smooths the input spot score tensor using iterative blurring until the mean change between iterations is below a specified threshold or a maximum number of iterations is reached.

        Args:
            spot_score (numpy.ndarray): Array containing spot scores.
            kernel_size (int): The size of the kernel for blurring.
            threshold (float, optional): The threshold for mean change between iterations. Defaults to 0.01.

        Returns:
            spot_score (numpy.ndarray): smoothed spot scores.
        """

        for i in range(spot_score.shape[0]):
            smooth_input = spot_score[i, :, :]  # Input for the first iteration
            nonzero_index_input = np.where(smooth_input != 0)
            mean_score_input = smooth_input[nonzero_index_input[0], nonzero_index_input[1]].mean()

            # Iterative blurring until mean change is less than threshold or max iterations reached
            for _ in range(10):
                smooth_output = cv2.blur(smooth_input, (kernel_size, kernel_size), cv2.BORDER_DEFAULT)
                diff_mat1 = (abs(smooth_input - smooth_output))
                nonzero_index = np.where(diff_mat1 != 0)
                mean_change = diff_mat1[nonzero_index[0], nonzero_index[1]].mean()

                smooth_input = smooth_output  # Update input for next iteration

                if mean_change < threshold: break

            mean_score_output = smooth_output[nonzero_index_input[0], nonzero_index_input[1]].mean()
            if mean_score_output < 0.01: mean_score_output = mean_score_input

            smooth_output = np.clip(smooth_output/mean_score_output * mean_score_input, 0, 1) if mean_score_output > 0 else smooth_output
            spot_score[i, :, :] = smooth_output  # Update the region with smoothed values

        return spot_score

    def get_VD_score(self,
                     use_score: str = 'GCN'):
        """
        Visualize domains for spatial transcriptomics data, optionally with spot-wise embedding.

        Args:
            use_score (str): The type of embedding to be visualized.
        """

        for name, section in self.sections.items():
            # Get the extended score
            extended_score = self._get_extended_score(section, use_score, use_all_pixel=False)

            # Get the coordinates for the tissue
            num_images = section.tissue_coord.shape[0]
            tmp_coords = section.tissue_coord.copy()
            tmp_coords[:, :2] -= section.row_range[0]
            tmp_coords[:, 2:] -= section.col_range[0]

            # Get the VD score for each patch
            VD_score = [extended_score[:, tmp_coords[i, 0]:tmp_coords[i, 1], tmp_coords[i, 2]:tmp_coords[i, 3]]
                        for i in range(num_images)]

            section.scores['VD'] = np.array(VD_score)

    def _get_extended_score(self,
                            section: spatial_obj,
                            use_score: str = 'GCN',
                            use_all_pixel: bool = False) -> np.ndarray:
        """
        Get the extended score for the given section.

        Args:
            section (spatial_obj): The spatial object.
            use_score (str): The type of embedding to be visualized.
            use_all_pixel (bool, optional): Whether to use all pixels or not. Defaults to False.

        Returns:
            extended_score (numpy.ndarray): Array of extended scores.
        """

        # Determine the range and nearby spots
        if use_all_pixel:
            row_range, col_range = (0, section.feasible_domain.shape[0]), (0, section.feasible_domain.shape[1])
            nearby_spots = section.all_nearby_spots
        else:
            row_range, col_range = section.row_range, section.col_range
            nearby_spots = section.vd_nearby_spots

        # Get the spot score, kernel size, and feasible domain
        spot_score = section.scores[use_score]
        kernel_size = section.kernel_size
        feasible_domain = section.feasible_domain[row_range[0]:row_range[1], col_range[0]:col_range[1]].astype(np.float32)

        # Get the extended score
        extended_score = np.reshape(spot_score[nearby_spots, :],
                                    (row_range[1] - row_range[0], col_range[1] - col_range[0], -1))
        extended_score = np.transpose(extended_score, (2, 0, 1))
        extended_score = self._smooth(extended_score, kernel_size, threshold=self.args.smooth_threshold)
        extended_score = extended_score * np.expand_dims(feasible_domain, axis=0)

        return extended_score

    def _prepare_train(self,
                       load_decoder_params: bool = True):
        """
        Prepare the training process for the DeepFuseNMF model.

        Args:
            load_decoder_params: Whether to load the decoder parameters or not.
        """

        # Prepare the training dataset
        self.train_dataset = torch.utils.data.ConcatDataset(
            [HE_Dataset(section=section, args=self.args) for name, section in self.sections.items()]
        )

        # Prepare the training loader
        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=self.args.batch_size, shuffle=True,
                                       drop_last=False, num_workers=0, collate_fn=lambda x: x)
        self.num_batches = len(self.train_loader)

        # Load the decoder parameters
        if load_decoder_params:
            self.model.nmf_decoder.data = torch.tensor(self.metagene.T, dtype=torch.float32, device=self.device,
                                                       requires_grad=True)

        # Set the model to training mode
        self.model.train()
        for name, p in self.model.named_parameters():
            p.requires_grad = True if 'image_pred' in name or 'low_rank' in name else False

        # Prepare the loss and optimizer
        self.loss_img = nn.MSELoss()
        self.loss_exp = nn.PoissonNLLLoss(log_input=False, reduction="mean")

        self.optimizer = Adam(self.model.parameters(), lr=self.args.lr, weight_decay=self.args.weight_decay)
        self.scheduler = CosineAnnealingLR(self.optimizer, T_max=self.args.fix_iter_train, eta_min=self.args.eta_min)

    def train(self,
              train_path: str):
        """
        Train the DeepFuseNMF model based on the image prediction and spot expression reconstruction.

        Args:
            train_path: The path to save the trained model.
        """

        self.model.training_mode = True

        if os.path.exists(train_path):
            print(f'*** Load trained model from {train_path} ***')
            self.model.load_state_dict(torch.load(train_path), strict=False)
        else:
            self._train_model()
            print(f'*** Save trained model to {train_path} ***')
            torch.save(self.model.state_dict(), train_path)

        # Save the NMF decoder parameters
        np.savetxt(f'{self.results_path}/V_para_train.csv',
                   np.array(self.model.nmf_decoder.data.cpu().detach().numpy().T), delimiter=",")

    def _train_model(self):
        # Train the DeepFuseNMF model

        self._prepare_train(load_decoder_params=True)

        if self.verbose: print('*** Training the model... ***')
        weight_image, weight_exp = 0.67, 0.33

        # Train the model
        rec_loss = rec_loss_image = rec_loss_exp = 0.

        epoch = current_iter = 0
        fix_flag = True
        while current_iter <= self.args.total_iter_train:
            if fix_flag and current_iter > self.args.fix_iter_train:
                for name, p in self.model.named_parameters():
                    p.requires_grad = True

                other_params = [param for name, param in self.model.named_parameters() if name not in ['gamma', 'nmf_decoder']]
                if self.reference is not None:
                    params = [{'params': other_params, 'lr': self.args.lr_train},
                              {'params': [self.model.gamma, self.model.nmf_decoder], 'lr': self.args.lr_train * 0.01}]
                else:
                    params = [{'params': other_params, 'lr': self.args.lr_train},
                              {'params': self.model.nmf_decoder, 'lr': self.args.lr_train * 0.01}]
                self.optimizer = Adam(params, weight_decay=self.args.weight_decay)
                self.scheduler = CosineAnnealingLR(self.optimizer, T_max=self.args.total_iter_train-current_iter,
                                                   eta_min=self.args.eta_min)
                fix_flag = False

            for data in self.train_loader:
                current_iter += 1
                loss = 0.

                for sub_img, spot_exp, feasible_coord, vd_score, section_name in data:
                    sub_img = torch.tensor(sub_img, dtype=torch.float32, device=self.device).unsqueeze(0)
                    vd_score = torch.tensor(vd_score, dtype=torch.float32, device=self.device).unsqueeze(0)
                    spot_exp = torch.tensor(spot_exp, dtype=torch.float32, device=self.device) if len(feasible_coord) > 0 else None

                    image_pred, spot_exp_pred, HR_score = self.model(sub_img, section_name, feasible_coord, vd_score)

                    # Calculate the loss
                    loss_image = self.loss_img(image_pred, sub_img) / len(data)
                    loss_exp = self.loss_exp(spot_exp_pred, spot_exp) / len(data) if spot_exp is not None else 0.

                    loss += weight_image * loss_image + weight_exp * loss_exp

                    # Regularization term
                    mask = torch.where(HR_score > 0.95)  # batch x rank x row x col
                    reg = F.mse_loss((1 - vd_score[mask]) ** 2 * HR_score[mask],
                                     (1 - vd_score[mask]) ** 2 * vd_score[mask]) if len(mask[0]) > 0 else 0
                    loss += 0.5 * reg / len(data)

                    rec_loss_image += loss_image
                    rec_loss_exp += loss_exp

                rec_loss += loss

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                self.scheduler.step()

                # Record the losses
                if self.verbose and current_iter % self.args.rec_iter == 0:
                    rec_loss = rec_loss.item() / self.args.rec_iter
                    rec_loss_image = rec_loss_image.item() / self.args.rec_iter
                    rec_loss_exp = rec_loss_exp.item() / self.args.rec_iter

                    print(f'[Iter: {current_iter} / {self.args.total_iter_train}], Epoch: {epoch + 1},'
                          f'Image Loss: {rec_loss_image:.6f}, Expression Loss: {rec_loss_exp:.6f}, Total Loss: {rec_loss:.6f},'
                          f'Learning rate: {self.scheduler.get_last_lr()[0]:.6e}')

                    rec_loss = rec_loss_image = rec_loss_exp = 0.

            epoch += 1

    def get_DeepFuseNMF_score(self,
                              save_score: bool=False):
        """
        Get the DeepFuseNMF scores for each section.

        Args:
            save_score (bool): Whether to save the DeepFuseNMF scores or not.
        """

        self.model.training_mode = True
        self.model.eval()

        for name, section in self.sections.items():
            if self.verbose: print(f'*** Extracting DeepFuseNMF scores for {name}... ***')

            image = section.image

            # Get the extended score
            extended_score = self._get_extended_score(section, use_all_pixel=True)

            # Get the DeepFuseNMF scores
            section.scores['DeepFuseNMF'] = self._extract_embedding(image, extended_score)

            if save_score:
                os.makedirs(section.save_paths['DeepFuseNMF'], exist_ok=True)
                np.save(f"{section.save_paths['DeepFuseNMF']}/DeepFuseNMF_score.npy", section.scores['DeepFuseNMF'])

            tmp_score = section.scores['DeepFuseNMF'] * 255
            tmp_score = tmp_score.astype(np.uint8)

            # Mask out the low signal regions
            section.mask = section.mask_init.copy()
            section.mask[np.where(tmp_score.sum(0) < 15)] = 0

        self.model.train()

    def _extract_embedding(self,
                           image: np.ndarray,
                           extended_score: np.ndarray) -> np.ndarray:
        """
        Extract the embedding based on the image and extended score.

        Args:
            image (numpy.ndarray): The image.
            extended_score (numpy.ndarray): The extended score.

        Returns:
            numpy.ndarray: The extracted embedding.
        """

        # Calculate the settings (e.g., bound width, overlap, etc.)
        bound_width = math.ceil(self.args.bound_ratio * self.args.split_size)
        frame = torch.zeros((self.args.split_size, self.args.split_size), dtype=torch.float16, device=self.device)
        frame[bound_width:-bound_width, bound_width:-bound_width] = 1

        dataset = HE_Score_Dataset(image, extended_score, self.args)
        dataloader = DataLoader(dataset, batch_size=4*self.args.batch_size, shuffle=False, num_workers=0)

        embeddings = np.zeros((self.rank, image.shape[1], image.shape[2]), dtype=np.float16)
        counts = torch.zeros((image.shape[1], image.shape[2]), dtype=torch.float16, device=self.device)

        for sub_images, sub_scores, start_rows, start_cols in dataloader:
            sub_images = sub_images.to(self.device)
            sub_scores = sub_scores.to(self.device)

            with torch.no_grad():
                sub_embeddings = self.model(sub_images, vd_score=sub_scores, encode_only=True).half()
                sub_embeddings = sub_embeddings * frame
                sub_embeddings = sub_embeddings.cpu().numpy()

            for i, (start_row, start_col) in enumerate(zip(start_rows, start_cols)):
                embeddings[:, start_row:start_row + self.args.split_size, start_col:start_col + self.args.split_size] += sub_embeddings[i]
                counts[start_row:start_row + self.args.split_size, start_col:start_col + self.args.split_size] += frame

        counts = counts.cpu().numpy()
        counts[counts == 0] = 1.

        # Return the average embeddings
        return embeddings / np.expand_dims(counts, axis=0)
