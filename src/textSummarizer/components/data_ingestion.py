import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):

        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

        if not os.path.exists(self.config.local_data_file):

            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} downloaded with info: {headers}")

        else:
            logger.info(
                f"File already exists of size: {get_size(self.config.local_data_file)}"
            )

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)