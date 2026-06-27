from pyspark.ml.classification import LogisticRegressionModel

MODEL_PATH = "models/logistic_regression_model"

def save_model(model):
    """
    Save trained Spark ML model.
    """
    model.write().overwrite().save(MODEL_PATH)
    print(f"Model saved successfully at {MODEL_PATH}")


if __name__ == "__main__":
    print(
        "Import this file inside train_logistic.py after model training."
    )