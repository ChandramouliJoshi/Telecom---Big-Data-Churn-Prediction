# Project File Structure

```text
Telecom - Big Data Churn Prediction/
├── data/
│   └── raw/
│       └── Telco_customer_churn.xlsx
├── docker/
├── models/
├── notebooks/
│   └── eda.ipynb
├── outputs/
├── src/
│   ├── config/
│   │   └── spark_config.py
│   ├── data_processing/
│   │   ├── load_data.py
│   │   └── validate_data.py
│   ├── deployment/
│   │   ├── batch_predict.py
│   │   └── save_pipeline.py
│   ├── feature_engineering/
│   │   ├── spark_sql_features.py
│   │   └── vector_assembler.py
│   ├── modeling/
│   │   ├── evaluate.py
│   │   ├── train_logistic.py
│   │   └── train_random_forest.py
│   └── utils/
│       └── logger.py
├── tele/
├── .gitignore
├── convert.py
├── main.py
├── README.md
├── requirements.txt
└── test.py
```
