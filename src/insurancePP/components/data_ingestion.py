import os
import urllib.request as request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from insurancePP.logging import logger
from insurancePP.utils.common import get_size
from insurancePP.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f'Downloaded {filename} to {self.config.local_data_file}')
        else:
            logger.info(f'File {self.config.local_data_file} already exists')


    def initiate_data_ingestion(self):
        logger.info("Entered inside the data ingestion component")

        try:
            data = pd.read_csv(self.config.local_data_file)
            logger.info("train test split initiated")

            train, test = train_test_split(data, test_size=0.2, random_state=50)
            train.to_csv(self.config.train_data_file)
            test.to_csv(self.config.test_data_file)
        except Exception as e:
            raise e