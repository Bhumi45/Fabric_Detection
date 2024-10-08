from training.configuration_manager.configuration import ConfigurationManager
from training.components.final_train.feature_engineering import FeatureEngineering
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Feature Engineering Training Pipeline"

class FeatureEngineeringTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            feature_engineering_config = config.get_feature_engineering_config()

            feature_engineering = FeatureEngineering(config=feature_engineering_config)
            
            # Transforming the data
            X_train, X_test, y_train, y_test, groups_train = feature_engineering.transform_features()

            # Saving the transformed data only if if does not exist
            if not X_train != None:
              feature_engineering.save_transformed_data(X_train,X_test, y_train, y_test, groups_train)
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>> {PIPELINE} started <<<<")
        obj = FeatureEngineeringTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)


