
import numpy as np
import pandas as pd
import os
import joblib
import sys
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from exception import CustomException
from logger import logging
from deployment.entity.config_entity import FeatureEngineeringConfig
from deployment.configuration_manager.configuration import ConfigurationManager


class FeatureEngineering:
    def __init__(self, config: FeatureEngineeringConfig) -> None:
        self.config = config


    def load_features(self):
        try:
            extracted_features_path = os.path.join(self.config.extracted_features, "X.npz")
            extracted_features = np.load(extracted_features_path)
            X = extracted_features['X']

            logging.info("Features loaded successfully")
            return X

        except Exception as e:
            raise CustomException(e, sys)
        
    def transform_features(self, X):
        logging.info("Features are now BEING transformed")


        pipeline_path = self.config.pipeline
        transform_pipeline = joblib.load(pipeline_path)
        
        X = transform_pipeline.transform(X)
        
        logging.info("Features NOW transformed")
        
        with open(self.config.STATUS_FILE,"w") as f:
            f.write(f"Feature engineering completed {True}")
            
        return X
    
    def save_transformed_data(self,X):

        transformed_data_path = self.config.root_dir
        np.savez(os.path.join(transformed_data_path, 'X.npz'), X=X)

        logging.info(f"Transformed Features have been saved to {transformed_data_path}")

        with open(self.config.STATUS_FILE,"w") as f:
          f.write(f"Feature engineering completed {True}")
    

if __name__ == "__main__":
    config = ConfigurationManager()
    feature_engineering_config = config.get_feature_engineering_config()
    feature_engineering = FeatureEngineering(config=feature_engineering_config)
    
    extracted_features = feature_engineering.load_features()
    transformed_features = feature_engineering.transform_features(extracted_features)
    feature_engineering.save_transformed_data(transformed_features)
