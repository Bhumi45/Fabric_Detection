import os
import sys
import cv2
from pathlib import Path
import shutil
from PIL import Image
from exception import CustomException
from logger import logging
from deployment.entity.config_entity import ImageProcessingConfig
from deployment.configuration_manager.configuration import ConfigurationManager


class ImageProcessing:
    def __init__(self, config: ImageProcessingConfig):
        self.config = config

    def process_uploaded_image(self):
        try:
            logging.info("Processing image...")

            # List all files in the directory
            for file_name in os.listdir(self.config.data_dir):
                if not file_name.endswith(('.jpg', '.png', '.jpeg')):
                    file_name += '.jpg'  # Default to .jpg if no valid extension is provided
                # Construct the full file path
                file_path = os.path.join(self.config.data_dir, file_name)

                # Try to load the file as an image
                image = cv2.imread(file_path)

                # Check if the file was loaded as a valid image
                if image is not None:
                    print(f"Loaded image: {file_name}")
                    

                    # Convert to grayscale
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    # Resize the image to the same dimensions as during training
                    image = cv2.resize(image, (128, 128))

                    return image

        except Exception as e:
            raise CustomException(e,sys)
        
    def save_image(self,image):
        try:
            # Save the image
            logging.info("Image processed & saved")
            
            # Save the image
            image_name =str(os.path.join(self.config.processed_images,"processed_image.jpg"))

            pil_image = Image.fromarray(image)
    
            # Save the image with Pillow
            pil_image.save(image_name)

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Image processing status: {True}")
        except Exception as e:
            raise CustomException(e,sys)
        
# To test the component
if __name__ == "__main__":
    config = ConfigurationManager()
    image_processing_config = config.get_image_processing_config()

    image_processing = ImageProcessing(config=image_processing_config)
    image = image_processing.process_uploaded_image()
    image_processing.save_image(image)

