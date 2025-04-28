from src.components.Data_ingestion import DataIngestion
import pandas as pd

df = DataIngestion().initiate_data_ingestion()

def objects_column(df):
  """
  This function takes a dataframe as input and returns a list of columns with object data type.
  """
  df_final = df.copy()
  col = []
  for i in df.columns:
    if df[i].dtype == 'object':
      col.append(i)
  df_final_1 = df_final[col]
  return df_final_1
