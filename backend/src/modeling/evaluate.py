from ..config.paths import RAW_CSV_PATH
from ..config.spark_config import create_spark_session

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

from pyspark.ml.evaluation import (
    MulticlassClassificationEvaluator,
    BinaryClassificationEvaluator
)

spark = create_spark_session()

# Load Dataset
df = spark.read.csv(
    str(RAW_CSV_PATH),
    header=True,
    inferSchema=True
)

# Select Features
df = df.select(
    "Gender",
    "Partner",
    "Dependents",
    "Contract",
    "Internet Service",
    "Tenure Months",
    "Monthly Charges",
    "CLTV",
    "Churn Value"
)

# Encode Categorical Columns
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
        "Contract_Index",
        "Internet_Index",
        "Tenure Months",
        "Monthly Charges",
        "CLTV"
    ],
    outputCol="features"
)

# Logistic Regression
lr = LogisticRegression(
    featuresCol="features",
    labelCol="Churn Value"
)

# Pipeline
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

# Train/Test Split
train_df, test_df = df.randomSplit(
    [0.8, 0.2],
    seed=42
)

# Train Model
model = pipeline.fit(train_df)

# Predictions
predictions = model.transform(test_df)

# Accuracy
accuracy = MulticlassClassificationEvaluator(
    labelCol="Churn Value",
    predictionCol="prediction",
    metricName="accuracy"
).evaluate(predictions)

# Precision
precision = MulticlassClassificationEvaluator(
    labelCol="Churn Value",
    predictionCol="prediction",
    metricName="weightedPrecision"
).evaluate(predictions)

# Recall
recall = MulticlassClassificationEvaluator(
    labelCol="Churn Value",
    predictionCol="prediction",
    metricName="weightedRecall"
).evaluate(predictions)

# F1 Score
f1_score = MulticlassClassificationEvaluator(
    labelCol="Churn Value",
    predictionCol="prediction",
    metricName="f1"
).evaluate(predictions)

# ROC AUC
auc = BinaryClassificationEvaluator(
    labelCol="Churn Value",
    rawPredictionCol="rawPrediction",
    metricName="areaUnderROC"
).evaluate(predictions)

print("\n===== MODEL EVALUATION =====")

print(f"Accuracy      : {accuracy:.4f}")
print(f"Precision     : {precision:.4f}")
print(f"Recall        : {recall:.4f}")
print(f"F1 Score      : {f1_score:.4f}")
print(f"ROC-AUC Score : {auc:.4f}")

spark.stop()
