from deployment.configuration_manager.configuration import ConfigurationManager
from deployment.components.feature_engineering import FeatureEngineering
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Feature Engineering Prediction Pipeline"

class FeatureEngineeringPredictionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            feature_engineering_config = config.get_feature_engineering_config()
            feature_engineering = FeatureEngineering(config=feature_engineering_config)
            
            extracted_features = feature_engineering.load_features()
            transformed_features = feature_engineering.transform_features(extracted_features)
            feature_engineering.save_transformed_data(transformed_features)
            
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>> {PIPELINE} started <<<<")
        obj = FeatureEngineeringPredictionPipeline()
        obj.main()
        logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)


