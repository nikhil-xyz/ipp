from insurancePP.components.data_validation import DataValidation
from insurancePP.config.configuration import ConfigurationManager
from insurancePP.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        validation_status = data_validation.validate_all_file_exist()