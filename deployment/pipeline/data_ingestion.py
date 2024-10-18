from deployment.configuration_manager.configuration import ConfigurationManager
from deployment.components.data_ingestion import DataIngestion
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Data Ingestion Prediction Pipeline"
class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            #Load the data ingestion configuration object
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()

            # Pass the data ingestion configuration obj to the Data Ingestion component
            data_ingestion = DataIngestion(config=data_ingestion_config)
        except Exception as e:
            raise CustomException(e, sys)


    

if __name__ == "__main__":
     try:
          logging.info(f">>>>> {PIPELINE} started <<<<")
          obj = DataIngestionPipeline()
          obj.main()
          logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
     except Exception as e:
          logging.error(e)
          raise CustomException(e,sys)
