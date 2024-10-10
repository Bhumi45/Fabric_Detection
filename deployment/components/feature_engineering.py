import numpy as np
import pandas as pd
import os
import joblib
import sys
from exception import CustomException



class FeatureEngineering:
    
    def __init__(self):
        pass

    def transform_features(self, extracted_features):

        pipeline_path = "artifacts/feature_engineering/pipeline.joblib"
        transform_pipeline = joblib.load(pipeline_path)
        extracted_features= extracted_features.reshape((1,-1))
        transformed_features = transform_pipeline.transform(extracted_features)
            
        return transformed_features
    
    