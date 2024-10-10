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
            image_processing = ImageProcessing()
            image = image_processing.process_image()

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