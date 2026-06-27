from src.config.spark_config import create_spark_session
from pyspark.ml.classification import LogisticRegressionModel

spark = create_spark_session()

MODEL_PATH = "models/logistic_regression_model"

model = LogisticRegressionModel.load(
    MODEL_PATH
)

df = spark.read.csv(
    "data/raw/Telco_customer_churn.csv",
    header=True,
    inferSchema=True
)

predictions = model.transform(df)

predictions.select(
    "CustomerID",
    "prediction",
    "probability"
).show(10, truncate=False)

predictions.select(
    "CustomerID",
    "prediction"
).write.mode("overwrite").csv(
    "outputs/predictions.csv",
    header=True
)

print(
    "Predictions saved successfully."
)

spark.stop()