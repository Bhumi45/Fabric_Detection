import cv2
import numpy as np
from deployment.exception import ImageProcessingError,handle_exception
from deployment.custom_logging import info_logger, error_logger
import os
import sys

class ImageProcessing:
    def __init__(self):
        pass

    def process_image(self, image):
        """
        Process the in-memory image passed from the PredictionPipeline.
        """
        try:
            # Convert to grayscale
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resize the image to the required dimensions (e.g., 128x128 for consistency)
            image_resized = cv2.resize(image_gray, (128, 128))

            return image_resized  # Return the processed image for further steps

        except Exception as e:
            handle_exception(e, ImageProcessingError)
