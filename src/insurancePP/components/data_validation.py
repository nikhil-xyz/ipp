from insurancePP.logging import logger
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from insurancePP.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config


    def validate_all_file_exist(self) -> bool:
        try:
            validation_status = False
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e
