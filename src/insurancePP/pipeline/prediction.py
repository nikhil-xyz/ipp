from insurancePP.components.model_prediction import ModelPrediction
from insurancePP.config.configuration import ConfigurationManager
from insurancePP.logging import logger


class PredictionPipeline:
    def __init__(self):
        pass

    def predicting_result(self, sample_df):
        try:
            config = ConfigurationManager()
            model_prediction_config = config.get_model_prediction_config()
            model_prediction = ModelPrediction(config = model_prediction_config)
            result = model_prediction.predict_sample_data(sample_df)
            return result
        except Exception as e:
            raise e