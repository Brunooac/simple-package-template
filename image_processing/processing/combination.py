from locale import normalize
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with the same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(
        gray_image1, gray_image2, full=True)
    print("Similarity of the images: ", score)
    normalize_difference_image = (difference_image-np.min(difference_image))/(
        np.max(difference_image)-np.min(difference_image))
    return normalize_difference_image


def trasfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, channel_axis=True)
    return matched_image
