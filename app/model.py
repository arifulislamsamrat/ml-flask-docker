import mlflow
from mlflow.tracking import MlflowClient
from app.config import Config

def load_production_model():
    """Load the latest production model from MLflow model registry"""
    client = MlflowClient()
    
    # Get latest production model version
    model_version = client.get_latest_versions(
        Config.MODEL_NAME,
        stages=[Config.STAGE]
    )[0]
    
    # Load the model
    model = mlflow.sklearn.load_model(f"models:/{Config.MODEL_NAME}/{Config.STAGE}")
    
    return model, model_version
