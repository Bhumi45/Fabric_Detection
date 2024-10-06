from dataclasses import dataclass
from pathlib import Path 

#1
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: Path
    data_dir: Path
    STATUS_FILE: str
#2
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    STATUS_FILE: str

#3
@dataclass(frozen=True)
class ImageProcessingConfig:
    root_dir: Path
    data_dir: Path
    STATUS_FILE: str

#4
@dataclass(frozen=True)
class FeatureExtractionConfig:
    root_dir: Path
    data_dir: Path
    STATUS_FILE: str

#5
@dataclass(frozen=True)
class FeatureEngineeringConfig:
    root_dir: Path
    data_dir: Path
    STATUS_FILE: str

#6
# Changes will be made as per the model is configured
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    #Hyperparameters
    alpha: float
    l1_ratio: float
    target_column: str
#7
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str