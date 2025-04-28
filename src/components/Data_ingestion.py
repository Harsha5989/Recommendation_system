import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)).rsplit('src', 1)[0])
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass


@dataclass
class DataIngestion:
  def initiate_data_ingestion(self) -> pd.DataFrame:
    logging.info("Data Ingestion started")
    try:
      
      df = pd.read_csv('data/dataset.csv')
      logging.info("Dataset read as dataframe")

      return df

    except Exception as e:
      raise CustomException(e, sys) from e
    

if __name__ == "__main__":
  obj = DataIngestion()
  obj.initiate_data_ingestion()