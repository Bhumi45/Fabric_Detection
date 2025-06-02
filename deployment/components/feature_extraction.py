import cv2
import numpy as np
import pandas as pd
import os
import sys
from skimage.feature import local_binary_pattern
from skimage.filters import gabor
from deployment.exception import FeatureExtractionError,handle_exception
from deployment.custom_logging import info_logger, error_logger


class FeatureExtraction:
    def __init__(self):
        pass

    @staticmethod
    def extract_canny_edge_detection(image):
        """ image must be passes to the function in grayscale"""
        # Step 1: Enhance contrast (optional)
        equalized_image = cv2.equalizeHist(image)

        # Step 2: Apply Gaussian Blur to reduce noise
        blurred_image = cv2.GaussianBlur(equalized_image, (3, 3), 1)

        # Step 3: Apply Canny Edge Detection with adjusted thresholds (convert back and forth)
        edges = cv2.Canny(blurred_image, 30, 30)

        return edges

    @staticmethod
    def extract_gabor_filters(image):
        """ image must be in grayscale"""

        def build_kernels():
            # Parameters
            gabor_kernels = []
            angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Use NumPy for angles
            ksize = 31  # Size of the filter
            sigma = 4.0  # Standard deviation of the Gaussian envelope
            lambd = 10.0  # Wavelength of the sinusoidal factor
            gamma = 0.5  # Spatial aspect ratio
            psi = 0  # Phase offset

            # Create Gabor kernels
            for theta in np.deg2rad([45, 135]):  # Convert degrees to radians
                kernel =cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)
                gabor_kernels.append(kernel)

            return gabor_kernels


        gabor_kernels = build_kernels()

        gabor_features = []

        for kernel in gabor_kernels:
            fimg = cv2.filter2D(image, cv2.CV_8UC3, kernel)
            gabor_features.append(fimg)

        gabor_features = np.array(gabor_features).flatten()

        return gabor_features
    
    @staticmethod
    def extract_local_binary_pattern(image):

        # Parameters
        radius = 1
        n_points = 8 * radius


        lbp = local_binary_pattern(image, n_points, radius, method="uniform")
        (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, n_points + 3),
                                range=(0, n_points + 2))
        hist = hist.astype("float")
        hist /= (hist.sum() + 1e-6)

        return hist
    

# Function to extract features from an image

    def extract_features(self,image):
        try:
            gray=image
            # Ensure the image is in grayscale
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Canny edge detection
            edges = self.extract_canny_edge_detection(gray)

            # Gabor Filter responses
            gabor_features = self.extract_gabor_filters(gray)

            # Local Binary Patterns (LBP)
            hist = self.extract_local_binary_pattern(gray)

            # Combine features: edges, Gabor, and LBP
            features = np.hstack([edges.flatten(), gabor_features, hist])

            return features  # Return features as NumPy array for further processing
        except Exception as e:
            handle_exception(e, FeatureExtractionError)
        

