import os
import sys
from pathlib import Path
import shutil
from exception import CustomException
from logger import logging
from training.entity.config_entity import DataIngestionConfig
from training.configuration_manager.configuration import ConfigurationManager

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def save_data(self):
        try:
            status = None
            if not os.path.exists(self.config.data_dir):
                shutil.copytree(self.config.source, self.config.data_dir)
                status = True

                with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Data Ingestion status: {status}")

                logging.info(f"Data Ingestion status: {status}")

            else:
                if not os.listdir(self.config.data_dir):
                    logging.info(f"Folder '{self.config.data_dir}' already exists and is empty, proceeding with copy...")

                    shutil.copytree(self.config.source, self.config.data_dir)
                    status = True

                    with open(self.config.STATUS_FILE, "w") as f:
                            f.write(f"Data Ingestion status: {status}")

                    logging.info(f"Data Ingestion status: {status}")

                else:
                    logging.info(f"Folder '{self.config.data_dir}' already exists and is not empty, aborting operation.")
                    status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Data Ingestion status: {status}")

        except CustomException as e:
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Data Ingestion status: {status}")
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()

    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.save_data()