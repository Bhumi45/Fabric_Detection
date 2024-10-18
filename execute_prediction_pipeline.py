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


PIPELINE = "Prediction Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    prediction = PredictionPipeline()

    # Assuming main() returns the predicted class number
    predicted_value = prediction.main()
    category_mapping = {1: 'corduroy', 2: 'denim', 3: 'lenin'}
    predicted_label = category_mapping.get(predicted_value, "Unknown")

    # Save the predicted label to a JSON file
    output = {
        'label': predicted_label
    }

    with open("artifacts_deployment/prediction/prediction_result.json", "w") as json_file:
        json.dump(output, json_file)

    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")

except Exception as e:
    logging.error(e)
    raise CustomException(e, sys)
