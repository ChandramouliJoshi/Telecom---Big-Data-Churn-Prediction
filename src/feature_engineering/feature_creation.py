"""
Feature vector assembly for the SparkScale Churn project.

Day 6 scope:
- Select the final set of model features (numeric + categorical).
- Index categorical columns into numeric form (required before assembly).
- Create the VectorAssembler that will combine features into a vector.

Day 7 scope:
- Fit and apply the StringIndexers and VectorAssembler.
- Generate the final `features` vector column.
- Verify feature vector dimensions and inspect sample output.

Day 8 scope:
- Run explain(True) on the transformed DataFrame to inspect the
  logical and physical execution plans.
- Trigger an action so the DAG is visible in the Spark UI for review.
"""

from typing import List

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline, PipelineModel

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

EXPECTED_FEATURE_DIMENSION = len(NUMERIC_FEATURE_COLUMNS) + len(
    CATEGORICAL_FEATURE_COLUMNS
)


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


def build_feature_pipeline() -> Pipeline:
    """
    Assemble the full feature engineering pipeline: StringIndexers for
    all categorical columns followed by the VectorAssembler.

    Returns:
        A Pipeline ready to be fit on the model-ready DataFrame.
    """
    indexers = build_string_indexers(CATEGORICAL_FEATURE_COLUMNS)
    assembler = build_vector_assembler(
        NUMERIC_FEATURE_COLUMNS, CATEGORICAL_FEATURE_COLUMNS
    )
    return Pipeline(stages=indexers + [assembler])


def generate_feature_vectors(model_df: DataFrame) -> DataFrame:
    """
    Fit the feature pipeline (indexers + assembler) on the model-ready
    DataFrame and apply it to generate the `features` vector column.

    Args:
        model_df: DataFrame with selected numeric and categorical columns.

    Returns:
        DataFrame with an added `features` vector column.
    """
    pipeline = build_feature_pipeline()
    pipeline_model: PipelineModel = pipeline.fit(model_df)
    return pipeline_model.transform(model_df)


def verify_feature_dimensions(transformed_df: DataFrame) -> None:
    """
    Verify that the generated `features` vectors have the expected
    dimension (one slot per numeric + categorical feature), and inspect
    sample rows for correctness.

    Args:
        transformed_df: DataFrame containing the `features` vector column.
    """
    sample_vector = transformed_df.select(OUTPUT_FEATURES_COLUMN).first()[
        OUTPUT_FEATURES_COLUMN
    ]
    actual_dimension = sample_vector.size

    print(f"Expected feature vector dimension: {EXPECTED_FEATURE_DIMENSION}")
    print(f"Actual feature vector dimension: {actual_dimension}")

    if actual_dimension == EXPECTED_FEATURE_DIMENSION:
        print("Feature dimension check PASSED.")
    else:
        print("Feature dimension check FAILED.")

    null_feature_count = transformed_df.filter(
        F.col(OUTPUT_FEATURES_COLUMN).isNull()
    ).count()
    print(f"Rows with null feature vectors: {null_feature_count}")

    print("Sample feature vectors:")
    transformed_df.select(
        "CustomerID", OUTPUT_FEATURES_COLUMN, "Churn Value"
    ).show(5, truncate=False)


def analyze_execution_plan(transformed_df: DataFrame) -> None:
    """
    Print the logical and physical execution plans for the transformed
    feature DataFrame, then trigger an action so the corresponding job
    and its DAG appear in the Spark UI (http://localhost:4040 by
    default) for visual review and screenshot capture.

    Args:
        transformed_df: DataFrame containing the `features` vector column.
    """
    print("=== Execution Plan (explain(True)) ===")
    transformed_df.explain(True)

    # Trigger an action so the plan above is actually executed as a job,
    # which makes the DAG visible under the "Jobs" / "SQL" tabs in the
    # Spark UI. Without an action, explain() only shows the plan and no
    # job is recorded for the DAG visualization.
    row_count = transformed_df.count()
    print(f"Triggered action: row count = {row_count}")
    print(
        "Open the Spark UI (default: http://localhost:4040) and check the "
        "'Jobs' tab for this run, then open the latest job's 'DAG "
        "Visualization' to capture the execution graph."
    )


def main() -> None:
    """
    Entry point: load data, create engineered features, select the
    final model feature set, generate feature vectors, verify their
    dimensions, and analyze the execution plan/DAG.
    """
    spark: SparkSession = create_spark_session()

    raw_df = load_raw_data(spark)
    enriched_df = add_charge_per_tenure(raw_df)
    model_df = select_model_features(enriched_df)

    transformed_df = generate_feature_vectors(model_df)
    verify_feature_dimensions(transformed_df)
    analyze_execution_plan(transformed_df)

    spark.stop()


if __name__ == "__main__":
    main()
