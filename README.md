# SparkScale Churn

## Scalable Telecom Customer Churn Prediction Using Apache Spark

SparkScale Churn is a Big Data Machine Learning project designed to predict customer churn for a telecom company using Apache Spark. The system processes large-scale customer datasets and builds a distributed machine learning pipeline capable of identifying customers likely to cancel their subscription.

---

## Problem Statement

Telecom companies generate massive amounts of customer data, including:

* Customer demographics
* Service subscriptions
* Billing information
* Usage behavior
* Contract details

Customer churn directly impacts revenue and customer acquisition costs. The objective of this project is to leverage Apache Spark's distributed computing capabilities to identify customers at risk of churn and support proactive retention strategies.

---

## Product Name

**SparkScale Churn**

---

## Project Objectives

* Build a scalable data processing pipeline using Apache Spark
* Perform data quality validation and preprocessing
* Engineer meaningful churn-related features
* Train machine learning models for churn prediction
* Evaluate model performance using Spark MLlib
* Deploy a reusable prediction pipeline

---

## Tech Stack

### Big Data

* Apache Spark
* Spark SQL
* Spark MLlib

### Programming Language

* Python 3

### Data Processing

* PySpark
* Pandas

### Machine Learning

* Logistic Regression
* Random Forest Classifier

### Deployment

* Docker

### Version Control

* Git
* GitHub

---

## Dataset

Dataset Used:

**Telco Customer Churn Dataset**

Dataset Characteristics:

* 7043 Customer Records
* 33 Features
* Customer Demographics
* Service Information
* Billing Details
* Churn Indicators

Target Variable:

```text
Churn Value

0 -> Customer Retained
1 -> Customer Churned
```

---

## Project Structure

```text
Telecom - Big Data Churn Prediction/

├── data/
│   └── raw/
│       └── Telco_customer_churn.csv
│
├── docker/
│
├── models/
│
├── notebooks/
│   └── eda.ipynb
│
├── outputs/
│
├── src/
│   ├── config/
│   │   └── spark_config.py
│   │
│   ├── data_processing/
│   │   ├── load_data.py
│   │   └── validate_data.py
│   │
│   ├── feature_engineering/
│   │   ├── spark_sql_features.py
│   │   ├── feature_creation.py
│   │   └── vector_assembler.py
│   │
│   ├── modeling/
│   │   ├── train_logistic.py
│   │   ├── train_random_forest.py
│   │   └── evaluate.py
│   │
│   ├── deployment/
│   │   ├── save_pipeline.py
│   │   └── batch_predict.py
│   │
│   └── utils/
│       └── logger.py
│
├── README.md
├── requirements.txt
└── main.py
```

---

## Project Workflow

### 1. Data Ingestion

* Load telecom customer dataset
* Infer schema automatically
* Validate dataset structure

### 2. Data Validation

* Missing value analysis
* Duplicate record detection
* Schema verification
* Data quality assessment

### 3. Feature Engineering

* Spark SQL analytics
* Customer behavior features
* Churn-related transformations
* Feature vector generation

### 4. Model Training

Models Implemented:

* Logistic Regression
* Random Forest Classifier

### 5. Evaluation

Performance Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### 6. Deployment

* Spark ML Pipeline
* Batch Prediction System
* Docker Containerization

---

## Team Responsibilities

### Person 1 – Data Processing

Files:

* spark_config.py
* load_data.py
* validate_data.py

Responsibilities:

* Spark Configuration
* Data Loading
* Data Quality Validation

### Person 2 – Feature Engineering

Files:

* spark_sql_features.py
* feature_creation.py
* vector_assembler.py

Responsibilities:

* Spark SQL
* Feature Engineering
* Feature Transformation

### Person 3 – Modeling & Deployment

Files:

* train_logistic.py
* train_random_forest.py
* evaluate.py
* save_pipeline.py
* batch_predict.py

Responsibilities:

* Model Training
* Evaluation
* Deployment Pipeline

---

## Installation

Create Virtual Environment

```bash
python -m venv tele
```

Activate Environment

```bash
tele\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run Data Validation

```bash
python -m src.data_processing.validate_data
```

Run Feature Engineering

```bash
python -m src.feature_engineering.spark_sql_features
```

Train Model

```bash
python -m src.modeling.train_logistic
```

Generate Predictions

```bash
python -m src.deployment.batch_predict
```

---

## Expected Outcome

The system predicts customer churn likelihood and enables telecom companies to identify high-risk customers before subscription cancellation, allowing proactive customer retention strategies.

---

## Future Enhancements

* Real-time streaming prediction using Spark Streaming
* Customer retention recommendation engine
* Model monitoring dashboard
* Cloud deployment on AWS or Azure
* Automated retraining pipeline

---

## Author

Developed as part of the Zaalima Internship Program.