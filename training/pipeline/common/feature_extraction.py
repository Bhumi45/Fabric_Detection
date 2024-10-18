from training.configuration_manager.configuration import ConfigurationManager
from training.components.common.feature_extraction import FeatureExtraction
from logger import logging
from exception import CustomException
import sys


PIPELINE = "Feature Extraction Training Pipeline"

class FeatureExtractionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            feature_extraction_config = config.get_feature_extraction_config()
            feature_extraction = FeatureExtraction(config=feature_extraction_config)
            feature_extraction.trigger_feature_extraction()
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    try:
        logging.info(f">>>>> {PIPELINE} started <<<<")
        obj = FeatureExtractionPipeline()
        obj.main()
        logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)