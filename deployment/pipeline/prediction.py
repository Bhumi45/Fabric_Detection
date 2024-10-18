from deployment.configuration_manager.configuration import ConfigurationManager
from deployment.components.prediction import Prediction
from logger import logging
from exception import CustomException
import sys

PIPELINE = "Prediction Pipeline"

class PredictionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prediction_config = config.get_prediction_config()
            prediction = Prediction(config=prediction_config)
            
            model = prediction.load_model()
            prediction = prediction.predict(model)
            
            return prediction
        
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>> {PIPELINE} started <<<<")
        obj = PredictionPipeline()
        obj.main()
        logging.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)


