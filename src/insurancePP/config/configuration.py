from insurancePP.constants import *
from insurancePP.utils.common import read_yaml, create_directories
from insurancePP.entity import (DataIngestionConfig,
                                DataValidationConfig,
                                DataTransformationConfig,
                                ModelTrainingConfig,
                                ModelPredictionConfig)   

class ConfigurationManager:
    def __init__(self, config_filepath= CONFIG_FILE_PATH, params_filepath= PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        # logger.info(f"Root directory {self.config.artifacts_root} created successfully") 
        
   
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            train_data_file = config.train_data_file,
            test_data_file = config.test_data_file
        )

        return data_ingestion_config


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )

        return data_validation_config


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            preprocessor_obj_file_path = config.preprocessor_obj_file_path,
            prepared_train_data = config.prepared_train_data,
            prepared_test_data = config.prepared_test_data
        )

        return data_transformation_config


    def get_model_training_configuration(self) -> ModelTrainingConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            prepared_train_data = config.prepared_train_data,
            prepared_test_data = config.prepared_test_data,
            preprocessor_obj_file_path = config.preprocessor_obj_file_path
        )

        return model_training_config


    def get_model_prediction_config(self) -> ModelPredictionConfig:
        config = self.config.model_prediction
        create_directories([config.root_dir])

        return ModelPredictionConfig(
            root_dir = config.root_dir,
            preprocessor_obj_file_path = config.preprocessor_obj_file_path,
            model_path = config.model_path
        )