from training.configuration_manager.configuration import ConfigurationManager
from training.components.common.data_validation import DataValidation
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Data Validation Training Pipeline"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            #Load the data validation configuration object
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()

            # Passing the data validation configuration obj to the component
            data_validation = DataValidation(config=data_validation_config)
            data_validation.check_al_data_is_images()
        except Exception as e:
            raise CustomException(e, sys)
            

"""
if __name__ == "__main__":
     try:
          logging.info(f">>>>> {PIPELINE} started <<<<")
          obj = DataValidationPipeline()
          obj.main()
          logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
     except Exception as e:
          logging.error(e)
          raise CustomException(e,sys)"""
