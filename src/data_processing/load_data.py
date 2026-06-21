from src.config.spark_config import create_spark_session

spark = create_spark_session()

df = spark.read.csv(
    r"C:\Zaalima Internship\Telecom - Big Data Churn Prediction\data\raw\Telco_customer_churn.csv",
    header=True,
    inferSchema=True
)

df.show(5)

df.printSchema()

print("Rows:", df.count())
print("Columns:", len(df.columns))

spark.stop()