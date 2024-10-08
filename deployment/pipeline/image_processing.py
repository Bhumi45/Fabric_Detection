from deployment.configuration_manager.configuration import ConfigurationManager
from deployment.components.image_processing import ImageProcessing
from logger import logging
from exception import CustomException
import sys


PIPELINE = "Image Processing Prediction Pipeline"

class ImageProcessingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            image_processing_config = config.get_image_processing_config()
            image_processing = ImageProcessing(config=image_processing_config)
            
            image = image_processing.process_uploaded_image()
            image_processing.save_image(image)

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    try:
        logging.info(f">>>>> {PIPELINE} started <<<<")
        obj = ImageProcessingPipeline()
        obj.main()
        logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)