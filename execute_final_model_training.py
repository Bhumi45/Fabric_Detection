from training.pipeline.common.data_ingestion import DataIngestionPipeline
from training.pipeline.common.data_validation import DataValidationPipeline
from training.pipeline.common.feature_extraction import FeatureExtractionPipeline
from training.pipeline.final_train.feature_engineering import FeatureEngineeringTrainingPipeline
from training.pipeline.final_train.model_trainer import ModelTrainingPipeline
from training.pipeline.final_train.model_evaluation import ModelEvaluationTrainingPipeline

from logger import logging
from exception import CustomException
import sys
import os

# ASSUMING THAT ONCE THE NESTED CROSS VALIDATION PIPELINE IS RUN THEN ONLY WE ARE RUNNING THIS PIPELINE
# OTHERWISE THIS PIPELINE WILL CRASH

PIPELINE = "Feature Engineering Training Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    feature_engineering = FeatureEngineeringTrainingPipeline()
    feature_engineering.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)


PIPELINE = "Final Model Training Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)


PIPELINE = "Final Model Evaluation Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)
