from insurancePP.components.data_transformation import DataTransformation
from insurancePP.config.configuration import ConfigurationManager
from insurancePP.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config = data_transformation_config)
            data_transformation.get_data_transformer_object()
            data_transformation.initiate_data_transformation()
            
        except Exception as e:
            raise e