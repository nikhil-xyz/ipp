from insurancePP.components.model_trainer import ModelTraining
from insurancePP.config.configuration import ConfigurationManager
from insurancePP.logging import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_training_config = config.get_model_training_configuration()
            model_trainer = ModelTraining(config = data_training_config)
            model_trainer.initiate_model_trainer()
            
        except Exception as e:
            raise e