import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI')
    MODEL_NAME = "iris-classifier"
    STAGE = "Production"