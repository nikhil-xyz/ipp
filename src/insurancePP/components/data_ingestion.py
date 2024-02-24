import os
import urllib.request as request
import zipfile
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