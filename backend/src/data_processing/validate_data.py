from pyspark.sql.functions import col, count, when
from pyspark.sql.types import StringType
from ..config.paths import RAW_CSV_PATH
from ..config.spark_config import create_spark_session

spark = create_spark_session()

# Load Dataset
df = spark.read.csv(
    str(RAW_CSV_PATH),
    header=True,
    inferSchema=True
)

print("\n===== DATASET INFORMATION =====")
print("Rows:", df.count())
print("Columns:", len(df.columns))

print("\n===== COLUMN DATA TYPES =====")
df.printSchema()

print("\n===== MISSING VALUES =====")

missing_counts = []

for column in df.columns:

    if isinstance(df.schema[column].dataType, StringType):

        missing_counts.append(
            count(
                when(
                    col(column).isNull() |
                    (col(column) == ""),
                    column
                )
            ).alias(column)
        )

    else:

        missing_counts.append(
            count(
                when(
                    col(column).isNull(),
                    column
                )
            ).alias(column)
        )

df.select(missing_counts).show(truncate=False)

print("\n===== DUPLICATE CUSTOMER CHECK =====")

total_rows = df.count()

unique_customers = (
    df.select("CustomerID")
      .distinct()
      .count()
)

print("Total Rows:", total_rows)
print("Unique Customers:", unique_customers)

if total_rows == unique_customers:
    print("No Duplicate Customer IDs Found")
else:
    print("Duplicate Customer IDs Detected")
print("\n===== DATASET READY STATUS =====")

critical_columns = [
    "CustomerID",
    "Tenure Months",
    "Monthly Charges",
    "Churn Value"
]

ready = True

for column in critical_columns:

    null_count = df.filter(
        col(column).isNull()
    ).count()

    if null_count > 0:
        ready = False
        print(
            f"FAIL - {column} contains {null_count} null values"
        )
    else:
        print(
            f"PASS - {column} validation passed"
        )

if total_rows == unique_customers:
    print("PASS - Customer uniqueness validation passed")
else:
    ready = False
    print("FAIL - Duplicate customer records found")

if ready:
    print("PASS - Critical feature validation passed")
    print("PASS - Dataset ready for feature engineering")
    print("PASS - Dataset ready for model training")

spark.stop()
