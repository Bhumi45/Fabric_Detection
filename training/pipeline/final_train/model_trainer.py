from training.configuration_manager.configuration import ConfigurationManager
from training.components.final_train.model_training import ModelTraining
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Final Model Training Pipeline"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            #Load the data ingestion configuration object
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            model_trainer = ModelTraining(config=model_trainer_config)

            # Loading the train data and test data for Final Training
            X_train, X_test, y_train,y_test, groups_train = model_trainer.load_transformed_data()

            # Selecting the best model for Final Training
            best_model_params = model_trainer.select_best_model(X_test,y_test)

            # Training the final model for Final Training
            final_model = model_trainer.train_final_model(best_model_params, X_train, y_train)

            # Save the final model for Final Training
            model_trainer.save_final_model(final_model)

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>> {PIPELINE} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)



