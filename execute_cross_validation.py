from training.pipeline.common.data_ingestion import DataIngestionPipeline
from training.pipeline.common.data_validation import DataValidationPipeline
from training.pipeline.common.feature_extraction import FeatureExtractionPipeline
from training.pipeline.cross_val.nested_cross_val import NestedCrossValPipeline

from logger import logging
from exception import CustomException
import sys
import os

PIPELINE = "Data Ingestion Training Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)


PIPELINE = "Data Validation Training Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)

PIPELINE = "Feature Extraction Training Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    feature_extraction = FeatureExtractionPipeline()
    feature_extraction.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)

PIPELINE = "Nested Cross ValidationTraining Pipeline"
try:
    logging.info(f">>>>> {PIPELINE} started <<<<")
    nested_cross_val = NestedCrossValPipeline()
    nested_cross_val.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)


