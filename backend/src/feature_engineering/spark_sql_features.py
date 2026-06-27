"""
Spark SQL based exploration for the SparkScale Churn project.

Day 1 scope:
- Load the raw telecom customer dataset.
- Inspect schema and columns.
- Validate the target column (`Churn Value`) for modeling readiness.

Day 2 scope:
- Register the dataset as a Spark SQL temporary view.
- Verify the temp view with simple validation queries.

Day 3 scope:
- Write aggregation queries: average tenure, average monthly charges,
  and contract type distribution, broken down by churn status.
"""

from pyspark.sql import DataFrame, SparkSession

from ..config.paths import RAW_CSV_PATH
from ..config.spark_config import create_spark_session

RAW_DATA_PATH = str(RAW_CSV_PATH)
TEMP_VIEW_NAME = "telco_customers"


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


def register_temp_view(df: DataFrame, view_name: str = TEMP_VIEW_NAME) -> None:
    """
    Register a DataFrame as a Spark SQL temporary view so it can be
    queried with SQL syntax.

    Args:
        df: DataFrame to register.
        view_name: Name to register the view under.
    """
    df.createOrReplaceTempView(view_name)


def verify_temp_view(spark: SparkSession) -> None:
    """
    Run simple validation queries against the temp view to confirm it
    was registered correctly and is queryable.

    Args:
        spark: Active SparkSession with the temp view already registered.
    """
    print(f"Verifying temp view `{TEMP_VIEW_NAME}`...")

    row_count = spark.sql(f"SELECT COUNT(*) AS row_count FROM {TEMP_VIEW_NAME}")
    print("Row count via SQL:")
    row_count.show()

    sample_rows = spark.sql(
        f"""
        SELECT CustomerID, Contract, `Tenure Months`, `Monthly Charges`, `Churn Value`
        FROM {TEMP_VIEW_NAME}
        LIMIT 5
        """
    )
    print("Sample rows via SQL:")
    sample_rows.show(truncate=False)


def get_average_tenure(spark: SparkSession) -> DataFrame:
    """
    Calculate average tenure (in months) grouped by churn status.

    Returns:
        DataFrame with columns: Churn Value, avg_tenure_months.
    """
    query = f"""
        SELECT
            `Churn Value`,
            ROUND(AVG(`Tenure Months`), 2) AS avg_tenure_months
        FROM {TEMP_VIEW_NAME}
        GROUP BY `Churn Value`
        ORDER BY `Churn Value`
    """
    return spark.sql(query)


def get_average_monthly_charges(spark: SparkSession) -> DataFrame:
    """
    Calculate average monthly charges grouped by churn status.

    Returns:
        DataFrame with columns: Churn Value, avg_monthly_charges.
    """
    query = f"""
        SELECT
            `Churn Value`,
            ROUND(AVG(`Monthly Charges`), 2) AS avg_monthly_charges
        FROM {TEMP_VIEW_NAME}
        GROUP BY `Churn Value`
        ORDER BY `Churn Value`
    """
    return spark.sql(query)


def get_contract_distribution(spark: SparkSession) -> DataFrame:
    """
    Calculate the distribution of customers across contract types,
    broken down by churn status.

    Returns:
        DataFrame with columns: Contract, Churn Value, customer_count,
        avg_monthly_charges.
    """
    query = f"""
        SELECT
            Contract,
            `Churn Value`,
            COUNT(*) AS customer_count,
            ROUND(AVG(`Monthly Charges`), 2) AS avg_monthly_charges
        FROM {TEMP_VIEW_NAME}
        GROUP BY Contract, `Churn Value`
        ORDER BY Contract, `Churn Value`
    """
    return spark.sql(query)


def run_aggregation_queries(spark: SparkSession) -> None:
    """
    Execute and display the Day 3 aggregation queries.

    Args:
        spark: Active SparkSession with the temp view already registered.
    """
    print("=== Average Tenure by Churn Status ===")
    get_average_tenure(spark).show(truncate=False)

    print("=== Average Monthly Charges by Churn Status ===")
    get_average_monthly_charges(spark).show(truncate=False)

    print("=== Contract Type Distribution by Churn Status ===")
    get_contract_distribution(spark).show(truncate=False)


def main() -> None:
    """
    Entry point: create a Spark session, load the raw dataset, run the
    Day 1 checks, register and verify the temp view (Day 2), then run
    the Day 3 aggregation queries.
    """
    spark = create_spark_session()

    raw_df = load_raw_data(spark)

    inspect_schema(raw_df)
    validate_target_column(raw_df)

    register_temp_view(raw_df)
    verify_temp_view(spark)

    run_aggregation_queries(spark)

    spark.stop()


if __name__ == "__main__":
    main()

