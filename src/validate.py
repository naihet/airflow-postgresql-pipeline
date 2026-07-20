import pandas as pd
from logger import logger

def validate_data(input_path):

    df = pd.read_parquet(input_path)

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": int(df.duplicated().sum()),
        "missing": df.isnull().sum().to_dict()
    }