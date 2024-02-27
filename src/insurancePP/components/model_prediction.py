from insurancePP.utils.common import load_object
from insurancePP.config.configuration import ModelPredictionConfig
from insurancePP.logging import logger


class ModelPrediction:
    def __init__(self, config : ModelPredictionConfig):
        self.config = config
        
    def predict_sample_data(self, data):
        preprocessor = load_object(self.config.preprocessor_obj_file_path)
        model = load_object(self.config.model_path)

        logger.info("Both preprocessor and model are loaded successfully from disk")
        return model.predict(preprocessor.transform(data))