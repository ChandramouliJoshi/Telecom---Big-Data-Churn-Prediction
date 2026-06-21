"""
Spark SQL based exploration for the SparkScale Churn project.

Day 1 scope:
- Load the raw telecom customer dataset.
- Inspect schema and columns.
- Validate the target column (`Churn Value`) for modeling readiness.
"""

from pyspark.sql import DataFrame, SparkSession

from src.config.spark_config import create_spark_session

RAW_DATA_PATH = "data/raw/Telco_customer_churn.csv"


def load_raw_data(spark: SparkSession, path: str = RAW_DATA_PATH) -> DataFrame:
    """
    Load the raw telecom customer dataset from CSV into a Spark DataFrame.

    Args:
        spark: Active SparkSession.
        path: Path to the raw CSV file.

    Returns:
        DataFrame containing the raw telecom customer records.
    """
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df


def inspect_schema(df: DataFrame) -> None:
    """
    Print the dataset schema and row/column counts for initial review.

    Args:
        df: Raw telecom customer DataFrame.
    """
    print(f"Total rows: {df.count()}")
    print(f"Total columns: {len(df.columns)}")
    print("Schema:")
    df.printSchema()


def validate_target_column(df: DataFrame) -> None:
    """
    Validate the `Churn Value` target column: confirm it only contains
    the expected binary values (0 = not churned, 1 = churned) and show
    the class distribution.

    Args:
        df: Raw telecom customer DataFrame.
    """
    print("Distinct values in target column `Churn Value`:")
    df.select("Churn Value").distinct().show()

    print("Class distribution for `Churn Value`:")
    df.groupBy("Churn Value").count().orderBy("Churn Value").show()


def main() -> None:
    """
    Entry point: create a Spark session, load the raw dataset, and run
    the Day 1 schema and target column checks.
    """
    spark = create_spark_session()

    raw_df = load_raw_data(spark)

    inspect_schema(raw_df)
    validate_target_column(raw_df)

    spark.stop()


if __name__ == "__main__":
    main()
