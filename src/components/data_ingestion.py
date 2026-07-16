import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def initiate_data_ingestion(self):
        logging.info("enter the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.config.train_data_path),exist_ok=True)
            df.to_csv(self.config.raw_data_path,index=False,header=True)

            logging.info("train test split")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.config. test_data_path,index=False,header=True)

            logging.info("ingestion of data is completed")
            return(
                self.config.train_data_path,
                self.config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    # Data Ingestion
    obj=DataIngestion(config=DataIngestionConfig())
    #save paths
    train_data_path, test_data_path=obj.initiate_data_ingestion()
    # Data Transformation
    transformer=DataTransformation(transformation_config=DataTransformationConfig())
    # Feed those paths into the transformation method
    train_arr,test_arr,_=transformer.initiate_data_transformation(train_data_path, test_data_path)
    # Model _training
    model_training=ModelTrainer(model_trainer_config=ModelTrainerConfig())
    #Feed the numerical arrays into the trainer
    final_score=model_training.initiate_model_trainer(train_arr,test_arr)
    
    logging.info(f"The best model's R2 score is: {final_score}")