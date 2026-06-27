from ..config.paths import RAW_CSV_PATH
from ..config.spark_config import create_spark_session

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

spark = create_spark_session()

# Load Dataset
df = spark.read.csv(
    str(RAW_CSV_PATH),
    header=True,
    inferSchema=True
)

# Select useful columns
selected_columns = [
    "Gender",
    "Partner",
    "Dependents",
    "Tenure Months",
    "Monthly Charges",
    "CLTV",
    "Contract",
    "Internet Service",
    "Churn Value"
]

df = df.select(*selected_columns)

# Convert categorical columns
gender_indexer = StringIndexer(
    inputCol="Gender",
    outputCol="Gender_Index"
)

partner_indexer = StringIndexer(
    inputCol="Partner",
    outputCol="Partner_Index"
)

dependents_indexer = StringIndexer(
    inputCol="Dependents",
    outputCol="Dependents_Index"
)

contract_indexer = StringIndexer(
    inputCol="Contract",
    outputCol="Contract_Index"
)

internet_indexer = StringIndexer(
    inputCol="Internet Service",
    outputCol="Internet_Index"
)

# Feature Vector
assembler = VectorAssembler(
    inputCols=[
        "Gender_Index",
        "Partner_Index",
        "Dependents_Index",
        "Tenure Months",
        "Monthly Charges",
        "CLTV",
        "Contract_Index",
        "Internet_Index"
    ],
    outputCol="features"
)

# Logistic Regression
lr = LogisticRegression(
    featuresCol="features",
    labelCol="Churn Value"
)

pipeline = Pipeline(
    stages=[
        gender_indexer,
        partner_indexer,
        dependents_indexer,
        contract_indexer,
        internet_indexer,
        assembler,
        lr
    ]
)

# Train-Test Split
train_df, test_df = df.randomSplit(
    [0.8, 0.2],
    seed=42
)

print("\nTraining Records:", train_df.count())
print("Testing Records:", test_df.count())

# Train Model
model = pipeline.fit(train_df)

# Generate Predictions
predictions = model.transform(test_df)

print("\n===== PREDICTION SUMMARY =====")

predictions.groupBy(
    "prediction"
    ).count().show()
print("\n===== SAMPLE PREDICTIONS =====")

predictions.select(
    "Churn Value",
    "prediction",
    "probability"
).show(10, truncate=False)

spark.stop()
