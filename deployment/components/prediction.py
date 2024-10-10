import numpy as np
import pandas as pd
import os
import joblib
import sys
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from exception import CustomException


class Prediction:

    def __init__(self):
        pass
        
    def predict(self, transformed_features):
        try:
            model_file_path = "artifacts/model_trainer/final_model.joblib"
            model = joblib.load(model_file_path)
            prediction  = model.predict(transformed_features)

            category_mapping = {1: 'corduroy', 2: 'denim', 3: 'linen'}
            predicted_label = category_mapping.get(prediction, "Unknown")

            return predicted_label
        
        except Exception as e:
            raise CustomException(e, sys)
        




