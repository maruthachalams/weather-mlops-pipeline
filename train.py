
import pandas as pd   
from sklearn.linear_model import LinearRegression 
import joblib
import mlflow
import mlflow.sklearn


mlflow.set_experiment("Coimbatore_weather_model")
with mlflow.start_run():
    data = {
        "day": [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],
        "temperature": [28, 29, 29, 30, 31, 31, 32, 33, 33, 34]
    }    

    model = LinearRegression()
    model.fit(data["day"], data["temperature"])

    accuracy = model.score(data["day"], data["temperature"])

    mlflow.log_param("algorithm", "LinearRegression")
    mlflow.log_metric("training_accuracy", accuracy)

    joblib.dump(model, "temperature_model.pkl")
    mlflow.sklearn.log_model(model, "model_artifact")

    print(f"Run tracked! Training Accuracy: {accuracy:.4f}")

