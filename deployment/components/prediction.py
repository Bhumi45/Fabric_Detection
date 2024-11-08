import numpy as np
import joblib
import pandas as pd
import sys
from deployment.exception import PredictionError,handle_exception
from deployment.custom_logging import info_logger, error_logger

class Prediction:

    def __init__(self):
        pass


    def predict(self, transformed_features):
        try:
            model_file_path = "artifacts/model_trainer/final_model.joblib"
            model = joblib.load(model_file_path)
            prediction  = model.predict(transformed_features)[0]
            #print(prediction)

            # Mapping prediction to category
            category_mapping = {1: 'corduroy', 2: 'denim'}
            predicted_label = category_mapping.get(prediction, "Unknown")

            return predicted_label

        except Exception as e:
            handle_exception(e, PredictionError)
