import os
import sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from exception import CustomException
from logger import logging
from training.entity.config_entity import FeatureEngineeringConfig
from training.configuration_manager.configuration import ConfigurationManager


class FeatureEngineering:
    def __init__(self, config: FeatureEngineeringConfig):
        self.config = config

    def transform_features(self):
        def proceed():
          transform_pipeline = Pipeline([
              ("scaler", StandardScaler()),
              ("pca",PCA(n_components=None))
          ])
          
          train_data_path = os.path.join(self.config.train_data_path,"Train.npz")
          test_data_path = os.path.join(self.config.test_data_path,"Test.npz")

          # Loading the .npz files
          train_data = np.load(train_data_path)
          test_data = np.load(test_data_path)

          X_train, y_train, groups_train = train_data["X_train"], train_data["y_train"], train_data["groups_train"]
          X_test, y_test = test_data["X_test"], test_data["y_test"]

          logging.info(f"Loaded Train.npz and Test.npz from {train_data_path} and {test_data_path}")

          # Fitting and transforming the train and test data
          transform_pipeline.fit(X_train)
          X_train = transform_pipeline.transform(X_train)
          X_test = transform_pipeline.transform(X_test)

          logging.info(f"Transformed X_train and X_test data using StandardScaler and PCA")

          return X_train, X_test, y_train, y_test, groups_train

        if os.path.exists(os.path.join(self.config.root_dir,"Train.npz")):
          if os.path.exists(os.path.join(self.config.root_dir,"Test.npz")):
            with open(self.config.STATUS_FILE,"w") as f:
              f.write(f"Feature engineering completed {True}")

            return None,None,None,None,None
          else:
            proceed()
        else:
          proceed()  
    
    def save_transformed_data(self,X_train, X_test, y_train, y_test, groups_train):
        transformed_data_path = self.config.root_dir

        np.savez(os.path.join(transformed_data_path, 'Train.npz'), X_train=X_train, y_train=y_train, groups_train=groups_train)
        np.savez(os.path.join(transformed_data_path, 'Test.npz'),  X_test=X_test, y_test=y_test)

        with open(self.config.STATUS_FILE,"w") as f:
          f.write(f"Feature engineering completed {True}")
         


