import os
import sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from exception import CustomException
from logger import logging
from training.entity.config_entity import ModelTrainerConfig
from training.configuration_manager.configuration import ConfigurationManager

import os
import sys
import cv2
from joblib import dump
from joblib import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, loguniform, randint
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupShuffleSplit
from sklearn.model_selection import GroupKFold
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report, f1_score


class ModelTraining:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config


    def load_transformed_data(self):
        logging.info("Loading the train data and test data for Final Training...")
        
        # Paths to the train and test .npz files
        train_data_path = os.path.join(self.config.train_data_path,"Train.npz")
        test_data_path = os.path.join(self.config.test_data_path,"Test.npz")

        # Loading the train and test .npz files
        train_data = np.load(train_data_path,allow_pickle=True)
        test_data = np.load(test_data_path, allow_pickle=True)

        # Access the arrays stored inside the .npz files
        X_train, y_train, groups_train = train_data["X_train"], train_data["y_train"], train_data["groups_train"]
        X_test, y_test = test_data["X_test"], test_data["y_test"]

        logging.info("Successfully Loaded the train data and test datafor Final Training...")

        return X_train, X_test, y_train,y_test, groups_train
    

    def select_best_model(self,X_test,y_test):

        logging.info("Selecting the best model for Final Training...")

        best_f1 = -1  # Initialize the best F1 score
        best_model = None  # Initialize the best model

        # Get the directory where models are stored
        model_dir = self.config.best_cross_val_models_rf

        # List all joblib files in the directory
        model_files = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if f.endswith('.joblib')]

        # Loop through all model file paths
        for model_path in model_files:
            # Load the model using joblib
            model = load(model_path)
            
            # Make predictions on the validation data
            logging.info(f"shape of X_test {X_test.shape}")
            logging.info(f"Type of X_test: {type(X_test)}")
            logging.info(f"Dtype of X_test : {X_test.dtype}")
            y_pred = model.predict(X_test)
            
            # Compute the macro average F1 score
            f1 = f1_score(y_test, y_pred, average='macro')
            
            # If the current model has the highest F1 score, update the best model
            if f1 > best_f1:
                best_f1 = f1
                best_model = model

        logging.info(f"Successfully selected the best model for Final Training... with macro_avg F1-score : {best_f1}")

        # Return the best model's hyperparameters 
        return best_model.get_params()

    def train_final_model(self,best_model_params, X_train, y_train):

        logging.info("Training the final model for Final Training...")
        # Initialize a new RandomForestClassifier with the best hyperparameters
        final_model = RandomForestClassifier(**best_model_params)

        final_model.fit(X_train,y_train)

        logging.info("Successfully trained the final model for Final Training...")

        return final_model


    def save_final_model(self, final_model):
        
        logging.info("Saving the final model for Final Training...")

        # Save the final model using joblib
        dump(final_model, self.config.final_model_name)

        with open(self.config.STATUS_FILE, "w") as f:
            f.write(f"Final Model status: {True}")

        logging.info("Successfully saved the final model for Final Training...")

        