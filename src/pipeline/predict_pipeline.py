import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from dataclasses import dataclass

class PredictPipeline:
    def __init__(self):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
           
            self.model = load_object(file_path=model_path)
            self.preprocessor = load_object(file_path=preprocessor_path)
            
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        
        try:
            data_scaled = self.preprocessor.transform(features)
            preds = self.model.predict(data_scaled)
            
            return preds
            
        except Exception as e:
            raise CustomException(e, sys)


@dataclass
class CustomData:
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            
            return pd.DataFrame(custom_data_input_dict)
            
        except Exception as e:
            raise CustomException(e, sys)