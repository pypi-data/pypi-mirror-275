import numpy as np
import pandas as pd
from PIL import Image
import cv2
import random
import torch
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from scipy.interpolate import make_interp_spline, BSpline
import scipy
from skan.pre import threshold
from skimage import morphology
from skan import draw
from skan.csr import skeleton_to_csgraph
from skan import Skeleton, summarize

class Bacteria_features_extractor:
    """
        Class contains functions to extract features from segmented bacteria images

        List of function:
        - menbrane_area
        - menbrane_perimeter
        - menbrane_length
        - membrane_width
        - membrane_circularity
        - sytoxG_intensity
        - DAPI_intensity
    """

    def __init__(self, default_unit:str = "micromet", pixel_length:float = 1.0):
        """
            Set default_unit and pixel_length in the output
        """
        self.default_unit = default_unit
        self.pixel_length = 1.0

    def maximum_intensity_projection(self, image:np.ndarray)->np.ndarray:
        """
            Function to get maximum intensity projection of the image
        """
        image_max = np.max(image, axis=2)
        return image_max

    def calculate_bacteria_area(self)->float:
        """
            Function to caculate bacteria area
        """
        area = cv2.contourArea(self.contour[0])
        return area
    
    def calculate_bacteria_perimeter(self)->float:
        """
            Function to calculate bacteria perimeter
        """
        perimeter = cv2.arcLength(self.contour[0], True)
        return perimeter
    
    def skeleton_analyze(self):
        """
            Analyze bacteria image using skeleton
        """
        spacing_nm = 1.0 * 1e9
        smooth_radius = 5 / 1e9  # float OK
        threshold_radius = int(np.ceil(50 / spacing_nm))
        binary0 = threshold(self.maximum_intensity_projected_image, sigma=smooth_radius,
                            radius=0)
        
        skeleton0 = morphology.skeletonize(binary0)
        self.branch_data = summarize(Skeleton(skeleton0))
    
    def analyze(self, image:np.ndarray):
        self.maximum_intensity_projected_image = self.maximum_intensity_projection(image)
        _, self.binary_image = cv2.threshold(self.maximum_intensity_projected_image, 0, 255, cv2.THRESH_BINARY)
        self.contour, _ = cv2.findContours(self.binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.membrane_area = self.calculate_bacteria_area()
        self.membrane_perimeter = self.calculate_bacteria_perimeter()
        self.skeleton_analyze()
        self.membrane_length = self.branch_data["branch-distance"]
