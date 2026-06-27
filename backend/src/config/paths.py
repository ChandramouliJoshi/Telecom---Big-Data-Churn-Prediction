from pathlib import Path


BACKEND_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = BACKEND_DIR / "data" / "raw"
RAW_CSV_PATH = RAW_DATA_DIR / "Telco_customer_churn.csv"
RAW_EXCEL_PATH = RAW_DATA_DIR / "Telco_customer_churn.xlsx"
