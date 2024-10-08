import os
import sys
from joblib import dump
from joblib import load
import json
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

from exception import CustomException
from logger import logging
from training.entity.config_entity import ModelEvaluationConfig
from training.configuration_manager.configuration import ConfigurationManager



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def load_test_data(self):
        logging.info("Loading the test data for Model Evaluation...")

        test_data_path = os.path.join(self.config.test_data_path,"Test.npz")

        # Loading the .npz files
        test_data = np.load(test_data_path)

        X_test, y_test = test_data["X_test"], test_data["y_test"]

        logging.info("Successfully loaded the test data for Model Evaluation...")

        return X_test, y_test

    def evaluate_final_model(self, final_model,X_test,y_test):
        logging.info("Evaluating final model...")

        y_pred = final_model.predict(X_test)

        report = classification_report(y_test,y_pred)

        with open(self.config.STATUS_FILE, "w") as f:
            f.write(report)

        # Generate classification report as a dictionary to save as metrics.json
        report_dict = classification_report(y_test, y_pred, output_dict=True)

        with open(self.config.metric_file_name, 'w') as f:
            json.dump(report_dict, f, indent=4)


        logging.info("Successfully evaluated the final model...")
