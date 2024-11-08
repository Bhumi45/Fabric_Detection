import numpy as np
import joblib
import pandas as pd
import os
from deployment.exception import FeatureEngineeringError,handle_exception
from deployment.custom_logging import info_logger, error_logger

class FeatureEngineering:
    
    def __init__(self):
        pass

    def transform_features(self, extracted_features):
        try:
            pipeline_path = "artifacts/feature_engineering/pipeline.joblib"
            transform_pipeline = joblib.load(pipeline_path)
            extracted_features= extracted_features.reshape((1,-1))
            transformed_features = transform_pipeline.transform(extracted_features)
                
            return transformed_features
        except Exception as e:
            handle_exception(e, FeatureEngineeringError)

    



