import pandas as pd
from logger import logger

def extract_data(csv_path, output_path):

    logger.info("Reading CSV file")

    df = pd.read_csv(
        csv_path,
        encoding="latin1"
    )

    logger.info(f"Extracted {len(df)} rows")

    df.to_parquet(
        output_path,
        index=False
    )

    logger.info("Raw parquet created")

    return output_path