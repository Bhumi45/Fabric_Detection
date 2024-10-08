import cv2
import numpy as np
import pandas as pd
import os
import sys
from skimage.feature import local_binary_pattern
from skimage.filters import gabor
from exception import CustomException
from logger import logging
from deployment.entity.config_entity import FeatureExtractionConfig
from deployment.configuration_manager.configuration import ConfigurationManager


class FeatureExtraction:
    def __init__(self, config: FeatureExtractionConfig) -> None:
        self.config = config

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
    @staticmethod
    def extract_features(image):
        # Convert to grayscale using NumPy arrays
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Canny edge detection
        edges = FeatureExtraction.extract_canny_edge_detection(gray)

        # Gabor Filter responses
        gabor_features=  FeatureExtraction.extract_gabor_filters(gray)

        # Local Binary Patterns (LBP)
        hist = FeatureExtraction.extract_local_binary_pattern(gray)

        # Combine features: edges, Gabor, and LBP
        features = np.hstack([edges.flatten(), gabor_features, hist])
        features = features

        return features # Return features back as NumPy array for further processing
    
    def save_features(self,X):
        # Convert lists to NumPy arrays
        X = np.array(X)

        # Convert the X array from float64to float16 
        X = X.astype(np.float16)
        
        # Path to the 'Extracted Features' directory
        save_dir = self.config.root_dir

        logging.info(f"Dtype of X: {X.dtype}")
        logging.info(f"Shape of X: {X.shape}")
        # Save each array as a separate .npz file
        np.savez(os.path.join(save_dir, 'X.npz'), X=X)

        logging.info(f"Features has been saved to {save_dir}")

        with open(self.config.STATUS_FILE, "w") as f:
            f.write(f"Feature Extraction status: {True}")


    def trigger_feature_extraction(self):
        try:
            # Setting up dataset_dir and categories variables
            dataset_dir = self.config.data_dir 
            X = []
            logging.info("Starting featuer extraction loop")

            
            # Reading the image
            img_name = os.listdir(dataset_dir)[0]
            img_path = os.path.join(dataset_dir, img_name)
            image = cv2.imread(img_path)


            # Extract features from the image
            original_features = self.extract_features(image)
            X.append(original_features)
            
            logging.info("Feature extraction completed successfully")
            
            self.save_features(X)
        except Exception as e:
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Feature Extraction status: {False}")
            raise CustomException(e, sys)            


if __name__ == "__main__":
    config = ConfigurationManager()
    feature_extraction_config = config.get_feature_extraction_config()
    feature_extraction = FeatureExtraction(config=feature_extraction_config)
    feature_extraction.trigger_feature_extraction()

