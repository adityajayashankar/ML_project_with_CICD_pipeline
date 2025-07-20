import os
import sys

from  src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig
#the entire thing below is an input to my data_ingestion component
@dataclass #will be able to directly define class variable 
class DataIngestionConfig:
 train_data_path: str=os.path.join("artifacts", "train.csv") #all the output will be saved in this path
 test_data_path: str=os.path.join("artifacts", "test.csv")
 raw_data_path: str=os.path.join("artifacts", "data.csv")
 
class DataIngestion:
 def __init__(self):
  self.ingestion_config = DataIngestionConfig() #all the 3 objects gets saved in this variable

 def initiate_data_ingestion(self): #this function is used to read the data from database
  logging.info("Entered the data ingestion method or component")
  try:
   df = pd.read_csv(r'C:\Users\adity\mlproject\notebook\data\stud.csv') #reading the data from the csv file
   logging.info("Read the dataset as dataframe")

   os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
   df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True) #saving the data in the raw_data_path
   logging.info("Train test split initiated")
   train_set,test_set = train_test_split(df,test_size=0.2,random_state=42) #splitting the data into train and test set
   train_set.to_csv(self.ingestion_config.train_data_path, index= False, header = True) #saving the train set in the train_data_path
   test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
   logging .info("Ingestion of the data is completed")

   return(
    self.ingestion_config.train_data_path,
    self.ingestion_config.test_data_path,
   
   )
  except Exception as e:
   raise CustomException(e,sys) #if there is any error in the above code, it will raise a custom exception with the error message and the system information
if __name__== "__main__":
 obj = DataIngestion()
 train_data, test_data = obj.initiate_data_ingestion() #calling the initiate_data_ingestion function to read the data from the csv file and split it into train and test set
#this is the main function which will be called when the script is run

data_transformation = DataTransformation()
train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

model_trainer = ModelTrainer()
print(model_trainer.initiate_model_trainer(train_arr, test_arr))