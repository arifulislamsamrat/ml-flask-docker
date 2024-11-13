import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.config import Config

def train_and_register_model():
    # Set MLflow tracking URI
    mlflow.set_tracking_uri(Config.MLFLOW_TRACKING_URI)
    
    # Start MLflow run
    with mlflow.start_run() as run:
        # Load and prepare data
        iris = load_iris()
        X = iris.data
        y = iris.target
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model
        accuracy = model.score(X_test, y_test)
        
        # Log parameters and metrics
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy)
        
        # Log model
        mlflow.sklearn.log_model(
            model,
            "model",
            registered_model_name=Config.MODEL_NAME
        )
        
        # Transition to production if accuracy is good enough
        client = MlflowClient()
        latest_version = client.get_latest_versions(Config.MODEL_NAME, stages=["None"])[0]
        
        if accuracy > 0.95:
            client.transition_model_version_stage(
                name=Config.MODEL_NAME,
                version=latest_version.version,
                stage="Production"
            )
        
        print(f"Model trained successfully! Test accuracy: {accuracy:.4f}")
        print(f"Run ID: {run.info.run_id}")

if __name__ == "__main__":
    train_and_register_model()