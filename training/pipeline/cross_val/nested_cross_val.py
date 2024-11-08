# Save X_train, X_test, y_train, y_test to be used by final_train

from training.configuration_manager.configuration import ConfigurationManager
from training.components.cross_val.nested_cross_val import NestedCrossVal
from training.custom_logging import info_logger
import sys
import gc

PIPELINE = "Nested Cross Validation Training Pipeline"

class NestedCrossValPipeline:

    def __init__(self):
        pass

    def main(self):
        #Load the data ingestion configuration object
        config = ConfigurationManager()
        nested_cross_val_config = config.get_nested_cross_val_config()

        # Pass the data ingestion configuration obj to the Data Ingestion component
        nested_cross_val = NestedCrossVal(config=nested_cross_val_config)

        # Loading the extracted features, labesl and groups
        X,y,groups = nested_cross_val.get_data_labels_groups()

        # Split the data into train and test sets
        X_train, X_test, y_train, y_test,groups_train = nested_cross_val.train_test_split(X,y,groups)

        # Save X_train, X_test, y_train, y_test to be used by final_train
        nested_cross_val.save_train_test_data_for_final_train(X_train, X_test, y_train, y_test, groups_train)

        # Initialize outer loop
        outer_cv = nested_cross_val.initialize_outer_loop()
        
        # outer_train_idx: Indices for the training data in the current fold
        # outer_val_idx: Indices for the testing data in the current fold

        # The following loops runs 2 times as the no of splits in outer_cv has been defined as 2
        count=1
        for outer_train_idx, outer_val_idx in outer_cv.split(X_train, y_train, groups=groups_train):
            # Train data for the current fold
            X_outer_train = X_train[outer_train_idx] # Training features
            y_outer_train = y_train[outer_train_idx] # Training lables
            groups_outer_train = groups_train[outer_train_idx] # Training groups

            # Validation data for the current fold
            X_outer_val = X_train[outer_val_idx] # Validation features
            y_outer_val = y_train[outer_val_idx] # Validation labels

            nested_cross_val.start_inner_loop(count,X_outer_train, y_outer_train, groups_outer_train, X_outer_val, y_outer_val)
            del X_outer_train
            del y_outer_train
            del groups_outer_train
            del X_outer_val
            del y_outer_val
            gc.collect()  # Collect garbage to free memory
            count+=1

        


if __name__ == "__main__":

    info_logger.info(f">>>>> {PIPELINE} started <<<<")
    obj = NestedCrossValPipeline()
    obj.main()
    info_logger.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")

