from deployment.components.image_processing import ImageProcessing
from deployment.components.feature_extraction import FeatureExtraction
from deployment.components.feature_engineering import FeatureEngineering
from deployment.components.prediction import Prediction
import sys
import os
import json

class PredictionPipeline:
    def __init__(self):
        pass

    def predict_label(self,image):

        image_processing = ImageProcessing()
        processed_image = image_processing.process_image(image)
        
        feature_extraction = FeatureExtraction()
        extracted_features = feature_extraction.extract_features(processed_image)

        feature_engineering = FeatureEngineering()
        transformed_features = feature_engineering.transform_features(extracted_features)

        prediction = Prediction()
        predicted_label = prediction.predict(transformed_features)
        
        return predicted_label


# PREDICTION

