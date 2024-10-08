import os
import sys
import cv2
from pathlib import Path
import shutil
from exception import CustomException
from logger import logging
from deployment.entity.config_entity import DataIngestionConfig
from deployment.configuration_manager.configuration import ConfigurationManager


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


if __name__ == "__main__":
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)