import math
import cv2
import pandas as pd
import numpy as np
from typing import List


class spatial_obj:
    """
    The spatial_obj class is used for handling and managing spatial data.

    Args:
        section_name (str): The name of the section.
        results_path (str): The path to save the results.
        image_path (str): The path to the image file.
        spot_coord_path (str): The path to the spot coordinates file.
        spot_exp_path (str): The path to the spot expression file.
        scale_factor (float): The scale factor.
        radius (float): The radius.
        multi_pages (bool): Whether to use multi-page mode.
        pages (List[int]): The list of page numbers.
        save_score (bool): Whether to save the score. Default is True.
        verbose (bool): Whether to enable verbose output. Default is False.

    Methods:
        load_spot_coord(spot_coord_path, scale_factor, radius): Load and scale spot coordinates, and filter out spots that are too close.
        prepare_feasible_domain(image_path, multi_pages, pages, scale_factor, spot_coord): Prepare the feasible domain for given spot coordinates.
        load_spot_exp(spot_exp_path, spot_coord, spot_index): Load spot expression data, and fill in zeros for extra spots.
    """

    def __init__(self,
                 section_name: str,
                 results_path: str,
                 image_path: str,
                 spot_coord_path: str,
                 spot_exp_path: str,
                 scale_factor: float,
                 radius: float,
                 multi_pages: bool = False,
                 pages: List[int] = None,
                 verbose: bool = False):

        # Assign the input parameters to the class attributes
        self.section_name = section_name
        self.scale_factor = scale_factor
        self.radius = int(radius / scale_factor)  # Calculate the radius based on the scale factor
        self.kernel_size = self.radius//2*2 + 1  # Calculate the kernel size based on the scale factor
        self.multi_pages = multi_pages
        self.pages = pages

        # If visualization is enabled, create directories for saving the results
        self.save_paths = {
            'NMF': f'{results_path}/{section_name}/NMF',
            'GCN': f'{results_path}/{section_name}/GCN',
            'DeepFuseNMF': f'{results_path}/{section_name}/DeepFuseNMF',
        }

        # Initialize a dictionary to store the scores
        self.scores = {'NMF': None, 'GCN': None, 'VD': None, 'DeepFuseNMF': None}
        if verbose: print(f"*** Prepare data for {section_name}... ***")

        # Load and process the spot coordinates
        self.spot_coord, self.spot_index, self.row_range, self.col_range = self.load_spot_coord(
            spot_coord_path=spot_coord_path,
            scale_factor=scale_factor,
            radius=self.radius)
        self.num_spots = self.spot_coord.shape[0]  # Number of spots

        # Prepare the feasible domain and load the image
        self.feasible_domain, self.image, self.mask_init = self.prepare_feasible_domain(image_path=image_path,
                                                                                        multi_pages=multi_pages,
                                                                                        pages=pages,
                                                                                        scale_factor=scale_factor,
                                                                                        spot_coord=self.spot_coord)

        # Load the spot expression data
        self.spot_exp = self.load_spot_exp(spot_exp_path=spot_exp_path, spot_coord=self.spot_coord,
                                           spot_index=self.spot_index)

        self.tissue_coord = None

    @staticmethod
    def load_spot_coord(spot_coord_path: str,
                        scale_factor: float,
                        radius: float):
        """
        Load and scale spot coordinates from a CSV file, and filter null spots based on distance criteria.

        Args:
            spot_coord_path (str): Directory path of the spot coordinates CSV file.
            scale_factor (float): Factor to scale the coordinates.
            radius (float): Radius to determine the threshold for null spots filtering.

        Returns:
            filtered_spot_coord (numpy.ndarray): An array of filtered spot coordinates.
            filtered_spot_index (numpy.ndarray): An array of filtered spot indices.
            row_range (tuple): A tuple containing the row range.
            col_range (tuple): A tuple containing the column range.
        """

        # Load and scale coordinates
        spot_coord = pd.read_csv(spot_coord_path, sep=",", header=0, index_col=0)
        spot_coord[['x_coord', 'y_coord']] = spot_coord.iloc[:, :2] / scale_factor

        # Continue using only coordinates for further calculations, keep 'type' for filtering
        spot_type = spot_coord['type'].values
        spot_coord = spot_coord[['x_coord', 'y_coord']]

        # Calculate pairwise distances between spots
        diff = spot_coord.values[:, np.newaxis, :] - spot_coord.values[np.newaxis, :, :]
        dist_mat = np.sqrt(np.sum(diff ** 2, axis=-1))

        # Determine null spots based on distance threshold
        threshold = radius * 6
        valid_spot_index = np.where(spot_type == 1)[0]
        null_spot_index = [i for i in np.where(spot_type == 0)[0] if
                           np.partition(dist_mat[i, valid_spot_index], 2)[1] < threshold]

        # Final spot selection
        spot_final_use_index = valid_spot_index.tolist() + null_spot_index
        filtered_spot_coord = spot_coord.iloc[spot_final_use_index]
        filtered_spot_index = filtered_spot_coord.index
        filtered_spot_coord = filtered_spot_coord.values - 1

        # Extract the minimum and maximum coordinates
        min_coords, max_coords = filtered_spot_coord.min(0), filtered_spot_coord.max(0)

        # Calculate the row and column ranges
        row_range = (int(min_coords[0] - radius), int(max_coords[0] + radius + 2))
        col_range = (int(min_coords[1] - radius), int(max_coords[1] + radius + 2))

        return filtered_spot_coord, filtered_spot_index, row_range, col_range

    @staticmethod
    def prepare_feasible_domain(image_path: str,
                                multi_pages: bool,
                                pages: List[int],
                                scale_factor: float,
                                spot_coord: pd.DataFrame):
        """
        Prepare feasible domains for given spot coordinates on a scaled image.

        Args:
            image_path (str): Directory path of the image file.
            multi_pages (bool): Whether to use multi-page mode.
            pages (List[int]): List of page numbers.
            scale_factor (float): Scaling factor for the image.
            spot_coord (DataFrame): DataFrame containing spot coordinates.

        Returns:
            feasible_domain (numpy.ndarray): An array indicating feasible domains for masking the visualization.
            image (numpy.ndarray): An array of the scaled image.
        """

        # Load and resize image
        if multi_pages:
            _, images = cv2.imreadmulti(image_path)
            image = np.zeros((images[0].shape[0], images[0].shape[1], len(pages)), dtype=np.uint8)
            for page in pages:
                image_cur = images[page]
                image[:, :, page] = image_cur[:, :, 0] if len(image_cur.shape) == 3 else image_cur
        else:
            image = cv2.imread(image_path)

        # Scale the image and normalize its values
        scaled_shape = (math.ceil(image.shape[0] / scale_factor), math.ceil(image.shape[1] / scale_factor))
        image = cv2.resize(image, (scaled_shape[1], scaled_shape[0])).astype(np.float32)
        image = np.transpose(image, (2, 0, 1)) / 255
        mask = np.zeros(scaled_shape, dtype=np.int32)
        background_value = image[:, 100:200, 100:200].mean(axis=(1, 2))
        mask[np.where(np.sum(np.abs(image - background_value[:, None, None]), axis=0) > 0.05)] = 1

        # Calculate pairwise distances between spots
        diffs = spot_coord[:, np.newaxis, :] - spot_coord[np.newaxis, :, :]
        dist_mat = np.sqrt(np.sum(diffs ** 2, axis=-1))
        dist_mat = np.nan_to_num(dist_mat, nan=10000)

        # Determine the larger radius for the distance threshold
        radius_big = math.ceil(np.sort(dist_mat[0, :])[1] * 1.1)
        distance_threshold = math.ceil(radius_big)

        # Create an array to mark feasible domains
        feasible_domain = np.zeros(scaled_shape, dtype=np.int32)
        for (row, col) in spot_coord:
            row, col = round(row), round(col)
            row_range = np.arange(max(row - distance_threshold, 0), min(row + distance_threshold + 1, scaled_shape[0]))
            col_range = np.arange(max(col - distance_threshold, 0), min(col + distance_threshold + 1, scaled_shape[1]))
            feasible_domain[np.ix_(row_range, col_range)] = 1

        mask = mask * feasible_domain
        return feasible_domain, image, mask

    @staticmethod
    def load_spot_exp(spot_exp_path: str,
                      spot_coord: pd.DataFrame,
                      spot_index: pd.Index):
        """
        Load spot expression data and extend it with zero-filled data for additional spots.

        Args:
            spot_exp_path (str): Directory path of the spot expression CSV file.
            spot_coord (DataFrame): DataFrame containing spot coordinates.

        Returns:
            spot_exp_extended (numpy.ndarray): An array of spot expression data, extended with zero-filled data for additional spots.
        """

        # Load expression data
        spot_exp = pd.read_csv(spot_exp_path, sep=",", header=0, index_col=0)

        # Prepare zero-filled DataFrame for extra spots
        num_extra_spots = spot_coord.shape[0] - spot_exp.shape[0]
        extra_spots = pd.DataFrame(np.zeros((num_extra_spots, spot_exp.shape[1])),
                                   index=spot_index[spot_exp.shape[0]:],
                                   columns=spot_exp.columns)

        # Concatenate original and extra spot data
        spot_exp_extended = pd.concat([spot_exp, extra_spots], axis=0)

        return spot_exp_extended.values
