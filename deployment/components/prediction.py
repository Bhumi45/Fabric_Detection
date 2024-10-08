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
from deployment.entity.config_entity import PredictionConfig
from deployment.configuration_manager.configuration import ConfigurationManager

class Prediction:
    def __init__(self, config: PredictionConfig):
        self.config = config

    def load_model(self) :
        try:
            logging.info(f"Loading model from {self.config.model_path}")
            model_file_path = self.config.model_path
            model = joblib.load(model_file_path)
            return model
        except Exception as e:
            raise CustomException(e, sys)
        
    def predict(self, model):
        try:
            features = np.load(self.config.data_dir)
            X = features['X']
            
            prediction  = model.predict(X)

            logging.info(f"prediction is {prediction}")
            return prediction
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    config = ConfigurationManager()
    prediction_config = config.get_prediction_config()
    prediction = Prediction(config=prediction_config)
    
    model = prediction.load_model()
    prediction = prediction.predict(model)
    
    # return prediction to API

