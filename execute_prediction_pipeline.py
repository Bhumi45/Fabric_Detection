from deployment.pipeline.data_ingestion import DataIngestionPipeline
from deployment.pipeline.image_processing import ImageProcessingPipeline
from deployment.pipeline.feature_extraction import FeatureExtractionPipeline
from deployment.pipeline.feature_engineering import FeatureEngineeringPredictionPipeline
from deployment.pipeline.prediction import PredictionPipeline

from logger import logging
from exception import CustomException
import sys
import os
import json

# ASSUMING THAT ONCE THE NESTED CROSS VALIDATION PIPELINE IS RUN THEN ONLY WE ARE RUNNING THIS PIPELINE
# OTHERWISE THIS PIPELINE WILL CRASH
PIPELINE = "Data Ingestion Prediction Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)


PIPELINE = "Image Processing Prediction Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    image_processing = ImageProcessingPipeline()
    image_processing.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)

PIPELINE = "Feature Extraction Prediction Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    feature_extraction = FeatureExtractionPipeline()
    feature_extraction.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)

PIPELINE = "Feature Engineering Prediction Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    feature_engineering = FeatureEngineeringPredictionPipeline()
    feature_engineering.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)


# PREDICTION
PIPELINE = "Prediction Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    prediction = PredictionPipeline()

    # Get prediction from the model
    predicted_value = prediction.main()  # Handle in-memory prediction
    category_mapping = {1: 'corduroy', 2: 'denim', 3: 'linen'}
    predicted_label = category_mapping.get(predicted_value, "Unknown")

    logging.info(f"Predicted Label: {predicted_label}")

    # Return the predicted label instead of saving it to a file
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    
    # Return the label so it can be passed to the Flask app

    # WE WILL NOT NEED JSON WILL REMOVE THIS SOON
    print(json.dumps({'label': predicted_label}))  # Output for Flask

except Exception as e:
    logging.error(e)
    raise CustomException(e, sys)
