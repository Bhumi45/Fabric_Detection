from training.configuration_manager.configuration import ConfigurationManager
from training.components.common.data_ingestion import DataIngestion
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Data Ingestion Training Pipeline"
class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        #Load the data ingestion configuration object
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        # Pass the data ingestion configuration obj to the Data Ingestion component
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.save_data()
        


    

"""if __name__ == "__main__":
    logging.info(f">>>>> {PIPELINE} started <<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
"""


