# Used to perform random tests

from training.components.feature_extraction import FeatureExtraction
from training.configuration_manager.configuration import ConfigurationManager
from training.utils.common import get_size
import os
from pathlib import Path
if __name__ == "__main__":
    """    config = ConfigurationManager()

    data_ingestion_config = config.get_feature_extraction_config()

    feature_extraction = FeatureExtraction(config=data_ingestion_config)

    print(feature_extraction.config.schema)"""
    print(f"Size of X is {get_size(Path("artifacts/feature_extraction/X.npz"))}")
    print(f"Size of y is {get_size(Path('artifacts/feature_extraction/y.npz'))}")
    print(f"Size of groups is {get_size(Path('artifacts/feature_extraction/groups.npz'))}")
