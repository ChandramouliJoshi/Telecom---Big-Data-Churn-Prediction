from pyspark.sql import SparkSession

def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("SparkScaleChurn")
        .getOrCreate()
    )

    return spark


if __name__ == "__main__":
    spark = create_spark_session()

    print("Spark Session Created Successfully")

    spark.stop()