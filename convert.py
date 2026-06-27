import pandas as pd
from backend.src.config.paths import RAW_CSV_PATH, RAW_EXCEL_PATH

df = pd.read_excel(
    RAW_EXCEL_PATH
)

df.to_csv(
    RAW_CSV_PATH,
    index=False
)

print("Conversion Successful")
