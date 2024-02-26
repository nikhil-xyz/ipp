from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    train_data_file: Path
    test_data_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    train_data_path : Path
    test_data_path : Path
    preprocessor_obj_file_path : Path
    prepared_train_data : Path
    prepared_test_data : Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir : Path
    model_path : Path
    prepared_train_data : Path
    prepared_test_data : Path
    preprocessor_obj_file_path : Path
    