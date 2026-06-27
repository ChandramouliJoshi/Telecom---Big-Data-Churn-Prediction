"""
Feature vector assembly for the SparkScale Churn project.

Day 6 scope:
- Select the final set of model features (numeric + categorical).
- Index categorical columns into numeric form (required before assembly).
- Create the VectorAssembler that will combine features into a vector.
"""

from typing import List

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from pyspark.ml.feature import StringIndexer, VectorAssembler

from src.config.spark_config import create_spark_session
from src.feature_engineering.spark_sql_features import load_raw_data
from src.feature_engineering.feature_creation import add_charge_per_tenure

# Numeric columns used directly in the model, including the engineered
# charge_per_tenure feature.
NUMERIC_FEATURE_COLUMNS: List[str] = [
    "Tenure Months",
    "Monthly Charges",
    "Total Charges",
    "charge_per_tenure",
]

# Binary (Yes/No) categorical columns, simple to index with two categories.
BINARY_CATEGORICAL_COLUMNS: List[str] = [
    "Senior Citizen",
    "Partner",
    "Dependents",
    "Phone Service",
    "Paperless Billing",
]

# Multi-class categorical columns requiring indexing.
MULTI_CLASS_CATEGORICAL_COLUMNS: List[str] = [
    "Contract",
    "Internet Service",
    "Payment Method",
]

CATEGORICAL_FEATURE_COLUMNS: List[str] = (
    BINARY_CATEGORICAL_COLUMNS + MULTI_CLASS_CATEGORICAL_COLUMNS
)

OUTPUT_FEATURES_COLUMN = "features"


def select_model_features(df: DataFrame) -> DataFrame:
    """
    Select and clean the final set of columns needed for modeling.

    `Total Charges` is loaded as a string in the raw dataset and contains
    blank values for customers with zero tenure, so it is cast to double
    and missing values are filled with 0.0.

    Args:
        df: DataFrame containing raw and engineered columns.

    Returns:
        DataFrame containing only the columns required for modeling,
        plus the identifier and target columns.
    """
    cleaned_df = df.withColumn(
        "Total Charges",
        F.when(F.trim(F.col("Total Charges")) == "", 0.0).otherwise(
            F.col("Total Charges").cast("double")
        ),
    )

    selected_columns = (
        ["CustomerID", "Churn Value"]
        + NUMERIC_FEATURE_COLUMNS
        + CATEGORICAL_FEATURE_COLUMNS
    )
    return cleaned_df.select(*selected_columns)


def build_string_indexers(categorical_columns: List[str]) -> List[StringIndexer]:
    """
    Build a StringIndexer for each categorical column. StringIndexer
    converts string category values into numeric indices, which is
    required because VectorAssembler only accepts numeric input columns.

    Args:
        categorical_columns: List of categorical column names to index.

    Returns:
        List of configured StringIndexer instances.
    """
    return [
        StringIndexer(
            inputCol=column,
            outputCol=f"{column}_index",
            handleInvalid="keep",
        )
        for column in categorical_columns
    ]


def build_vector_assembler(
    numeric_columns: List[str], categorical_columns: List[str]
) -> VectorAssembler:
    """
    Create the VectorAssembler that combines numeric features and
    indexed categorical features into a single `features` vector column.

    Args:
        numeric_columns: Numeric feature column names.
        categorical_columns: Categorical column names (pre-indexing).

    Returns:
        Configured VectorAssembler instance.
    """
    indexed_columns = [f"{column}_index" for column in categorical_columns]
    input_columns = numeric_columns + indexed_columns

    return VectorAssembler(
        inputCols=input_columns,
        outputCol=OUTPUT_FEATURES_COLUMN,
        handleInvalid="keep",
    )


def main() -> None:
    """
    Entry point: load data, create engineered features, select the
    final model feature set, and set up the StringIndexers and
    VectorAssembler for the modeling pipeline.
    """
    spark: SparkSession = create_spark_session()

    raw_df = load_raw_data(spark)
    enriched_df = add_charge_per_tenure(raw_df)
    model_df = select_model_features(enriched_df)

    print("Selected model feature columns:")
    print(model_df.columns)

    indexers = build_string_indexers(CATEGORICAL_FEATURE_COLUMNS)
    print(f"Created {len(indexers)} StringIndexer stages for categorical columns:")
    for indexer in indexers:
        print(f"  {indexer.getInputCol()} -> {indexer.getOutputCol()}")

    assembler = build_vector_assembler(
        NUMERIC_FEATURE_COLUMNS, CATEGORICAL_FEATURE_COLUMNS
    )
    print(f"VectorAssembler input columns ({len(assembler.getInputCols())}):")
    print(assembler.getInputCols())
    print(f"VectorAssembler output column: {assembler.getOutputCol()}")

    spark.stop()


if __name__ == "__main__":
    main()
