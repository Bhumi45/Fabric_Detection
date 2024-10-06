# Used to perform random tests

from training.components.feature_extraction import FeatureExtraction
from training.configuration_manager.configuration import ConfigurationManager

import os
if __name__ == "__main__":
    config = ConfigurationManager()

    data_ingestion_config = config.get_feature_extraction_config()

    feature_extraction = FeatureExtraction(config=data_ingestion_config)

    print(feature_extraction.config.schema)