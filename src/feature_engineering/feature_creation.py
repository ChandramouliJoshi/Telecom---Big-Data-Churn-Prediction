"""
Feature creation for the SparkScale Churn project.

Day 4 scope:
- Create the engineered feature `charge_per_tenure`.
- Validate the generated feature for correctness and edge cases.

Day 5 scope:
- Convert `Churn Label` (Yes/No) into a binary `churn_binary` column.
- Validate the binary label against the existing `Churn Value` column.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

from src.config.spark_config import create_spark_session
from src.feature_engineering.spark_sql_features import load_raw_data


def add_charge_per_tenure(df: DataFrame) -> DataFrame:
    """
    Create the `charge_per_tenure` engineered feature, defined as
    Monthly Charges divided by Tenure Months.

    Customers with zero tenure (new sign-ups) would cause a divide-by-zero
    error, so for those rows `charge_per_tenure` is set equal to their
    Monthly Charges instead (their first month's spend rate).

    Args:
        df: Raw telecom customer DataFrame.

    Returns:
        DataFrame with an added `charge_per_tenure` column.
    """
    return df.withColumn(
        "charge_per_tenure",
        F.when(
            F.col("Tenure Months") == 0,
            F.col("Monthly Charges"),
        ).otherwise(
            F.round(F.col("Monthly Charges") / F.col("Tenure Months"), 2)
        ),
    )


def validate_charge_per_tenure(df: DataFrame) -> None:
    """
    Validate the `charge_per_tenure` feature: check for nulls, confirm
    no negative or infinite values, and show summary statistics.

    Args:
        df: DataFrame containing the `charge_per_tenure` column.
    """
    null_count = df.filter(F.col("charge_per_tenure").isNull()).count()
    print(f"Null values in charge_per_tenure: {null_count}")

    negative_count = df.filter(F.col("charge_per_tenure") < 0).count()
    print(f"Negative values in charge_per_tenure: {negative_count}")

    zero_tenure_count = df.filter(F.col("Tenure Months") == 0).count()
    print(f"Customers with zero tenure (handled separately): {zero_tenure_count}")

    print("Summary statistics for charge_per_tenure:")
    df.select("charge_per_tenure").describe().show()

    print("Sample rows with the new feature:")
    df.select(
        "CustomerID",
        "Tenure Months",
        "Monthly Charges",
        "charge_per_tenure",
        "Churn Value",
    ).show(10, truncate=False)


def add_binary_churn_label(df: DataFrame) -> DataFrame:
    """
    Convert the `Churn Label` column (Yes/No) into a binary integer
    column `churn_binary` (Yes -> 1, No -> 0).

    Args:
        df: Raw telecom customer DataFrame containing `Churn Label`.

    Returns:
        DataFrame with an added `churn_binary` column.
    """
    return df.withColumn(
        "churn_binary",
        F.when(F.col("Churn Label") == "Yes", F.lit(1))
        .when(F.col("Churn Label") == "No", F.lit(0))
        .otherwise(F.lit(None).cast("integer")),
    )


def validate_binary_churn_label(df: DataFrame) -> None:
    """
    Validate the `churn_binary` column: check for nulls (unexpected
    `Churn Label` values) and confirm it matches the existing
    `Churn Value` column exactly.

    Args:
        df: DataFrame containing both `churn_binary` and `Churn Value`.
    """
    null_count = df.filter(F.col("churn_binary").isNull()).count()
    print(f"Null values in churn_binary (unexpected Churn Label values): {null_count}")

    print("Distribution of churn_binary:")
    df.groupBy("churn_binary").count().orderBy("churn_binary").show()

    mismatch_count = df.filter(
        F.col("churn_binary") != F.col("Churn Value")
    ).count()
    print(f"Rows where churn_binary differs from Churn Value: {mismatch_count}")

    print("Sample rows comparing churn_binary to Churn Value:")
    df.select("CustomerID", "Churn Label", "churn_binary", "Churn Value").show(
        10, truncate=False
    )


def main() -> None:
    """
    Entry point: create a Spark session, load the raw dataset, create
    the engineered features (Day 4 and Day 5), and validate them.
    """
    spark: SparkSession = create_spark_session()

    raw_df = load_raw_data(spark)

    enriched_df = add_charge_per_tenure(raw_df)
    validate_charge_per_tenure(enriched_df)

    enriched_df = add_binary_churn_label(enriched_df)
    validate_binary_churn_label(enriched_df)

    spark.stop()


if __name__ == "__main__":
    main()
