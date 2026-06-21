import pandas as pd

df = pd.read_excel(
    r"C:\Zaalima Internship\Telecom - Big Data Churn Prediction\data\raw\Telco_customer_churn.xlsx"
)

df.to_csv(
    "data/raw/Telco_customer_churn.csv",
    index=False
)

print("Conversion Successful")