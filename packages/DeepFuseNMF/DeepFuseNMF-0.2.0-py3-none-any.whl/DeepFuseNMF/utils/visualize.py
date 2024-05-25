import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
from pkg_resources import resource_filename
from ..data import spatial_obj

# Load color map
data_file_path = resource_filename(__name__, 'color.csv')
color_map = pd.read_csv(data_file_path, header=0)
blue2red = np.array(
    [(int(color[5:7], 16), int(color[3:5], 16), int(color[1:3], 16)) for color in color_map['blue2red'].values],
    dtype=np.uint8)
blue2yellow = np.array(
    [(int(color[5:7], 16), int(color[3:5], 16), int(color[1:3], 16)) for color in color_map['blue2yellow'].values],
    dtype=np.uint8)


def visualize_score(sections,
                    use_score: str,
                    index: int = None,
                    scale: float = 4.,
                    verbose: bool = False):
    """
    save score for given spot coordinates and region scores.

    Args:
        sections: Spatial_obj or dictionary containing the sections.
        use_score (str): The type of embedding to be visualized.
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
        GMM_filter (bool, optional): Whether to use Gaussian Mixture Model for filtering low signal. Defaults to False.
        verbose (bool, optional): Whether to enable verbose output. Defaults to False.
    """

    if verbose: print(f"*** Visualizing the embeddings of {use_score}... ***")

    if type(sections) == spatial_obj:
        sections = {sections.section_name: sections}

    # Visualize the embeddings of each section
    for _, section in sections.items():
        # Get section attributes
        feasible_domain = section.feasible_domain
        spot_score = section.scores[use_score]
        save_path = section.save_paths[use_score]

        # Visualize DeepFuseNMF embeddings
        if 'DeepFuseNMF' in use_score:
            visualize_deepfusenmf(all_score=spot_score, save_path=save_path + '/absolute/', index=index, scale=scale,
                                  mask=section.mask, feasible_domain=feasible_domain, cutoff_type="absolute_value")
            visualize_deepfusenmf(all_score=spot_score, save_path=save_path + '/quantile/', index=index, scale=scale,
                                  mask=section.mask, feasible_domain=feasible_domain, cutoff_type="quantile")
            continue

        # Get spot coordinates and nearby spots
        if use_score == 'NMF':
            spot_coord, nearby_spots = section.spot_coord, section.nearby_spots
        else:
            spot_coord, nearby_spots = section.all_spot_coord, section.all_nearby_spots

        # Perform visualization
        visualize_domains(nearby_spots=nearby_spots, spot_score=spot_score, index=index,
                          save_path=save_path, feasible_domain=feasible_domain)


def visualize_domains(nearby_spots: np.ndarray,
                      spot_score: np.ndarray,
                      save_path: str,
                      feasible_domain: np.ndarray,
                      index: int = None):
    """
    Visualize domains for spatial transcriptomics data.

    Args:
        nearby_spots (numpy.ndarray): Array containing nearby spots.
        spot_score (numpy.ndarray): Array containing spot scores or region profiles.
        save_path (str): Path where the visualizations will be saved.
        feasible_domain (numpy.ndarray): Array indicating feasible domains for masking the visualization.
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
    """

    # Get extended score and reshape
    row_range, col_range = feasible_domain.shape
    extended_score = spot_score[nearby_spots, :]
    reshaped_score = np.reshape(extended_score, (row_range, col_range, spot_score.shape[1]))

    # Visualize embedding for each dimension
    for idx in range(spot_score.shape[1]):
        if index is not None: idx = index

        tmp_score = reshaped_score[:, :, idx]
        normalized_score = tmp_score / tmp_score.max() * 255
        filtered_score = normalized_score * feasible_domain

        # Visualize score of the specific index
        if index is not None:
            plt.imshow(filtered_score, cmap='gray_r')
            plt.show()
            break

        cv2.imwrite(f"{save_path}/region_scale_spot_{idx}.png", filtered_score)


def visualize_deepfusenmf(all_score: np.ndarray,
                          save_path: str,
                          scale: float,
                          mask: np.ndarray,
                          feasible_domain: np.ndarray,
                          cutoff_type: str = "absolute_value",
                          index: int = None):
    """
    Visualize domains for DeepFuseNMF embeddings.

    Args:
        all_score (numpy.ndarray): Array containing all scores.
        save_path (str): Path where the visualizations will be saved.
        feasible_domain (numpy.ndarray): Array indicating feasible domains for masking the visualization.
        cutoff_type (str, optional): The type of cutoff to be used. Defaults to "absolute_value".
        index (int, optional): The index of the embedding to be visualized. Defaults to None.
    """

    # Create directory if not exists
    if index is None:
        os.makedirs(save_path, exist_ok=True)
        os.makedirs(save_path + '/gray', exist_ok=True)
        os.makedirs(save_path + '/color', exist_ok=True)

    # Determine the pixel for max and min value
    mask = np.where(mask == 1)
    row_range, col_range = (mask[0].min(), mask[0].max() + 1), (mask[1].min(), mask[1].max() + 1)
    tmp_score = np.zeros_like(feasible_domain, dtype=np.uint8)
    tmp_score[mask] = 1

    tmp_score = tmp_score[row_range[0]:row_range[1], col_range[0]:col_range[1]]
    tmp_score = cv2.resize(tmp_score, (int(tmp_score.shape[1] / scale), int(tmp_score.shape[0] / scale)), interpolation=cv2.INTER_NEAREST)
    background = np.where(tmp_score == 0)

    # Visualize DeepFuseNMF embeddings for each dimension
    for idx in range(all_score.shape[0]):
        if index is not None: idx = index

        region_score = all_score[idx, :, :]
        region_max = 1 if cutoff_type == "absolute_value" else np.quantile(region_score[np.where(feasible_domain == 1)], 0.99)

        # Normalize
        normalized_score = region_score / region_max * 255

        # Apply feasible domains filtering
        filtered_score = normalized_score * feasible_domain

        # Visualize score of the specific index
        if index is not None:
            plt.imshow(filtered_score, cmap='gray_r')
            plt.show()
            break

        cv2.imwrite(f"{save_path}/gray/region_scale_spot_{idx}.png", filtered_score)

        # Colorize the score
        color_map_array = blue2red
        filtered_score = filtered_score[row_range[0]:row_range[1], col_range[0]:col_range[1]]

        filtered_score = cv2.resize(filtered_score,
                                    (int(filtered_score.shape[1] / scale), int(filtered_score.shape[0] / scale)))

        color_img = color_map_array[filtered_score.astype(np.uint8)]

        # Set the color of the background to gray
        color_img[background] = [128, 128, 128]

        # Save the colorized score image
        cv2.imwrite(f"{save_path}/color/region_scale_spot_{idx}.png", color_img)
