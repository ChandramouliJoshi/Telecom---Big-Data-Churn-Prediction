from pyspark.sql.functions import col, count, when
from pyspark.sql.types import StringType
from src.config.spark_config import create_spark_session

spark = create_spark_session()

# Load Dataset
df = spark.read.csv(
    "data/raw/Telco_customer_churn.csv",
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

spark.stop()