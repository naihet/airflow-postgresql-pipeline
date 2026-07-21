import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text
from src.logger import logger
from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine

def get_engine():

    conn = BaseHook.get_connection("sales_db")

    engine = create_engine(

        f"postgresql://{conn.login}:{conn.password}"
        f"@{conn.host}:{conn.port}/{conn.schema}"

    )

    return engine

def load_data(input_path):

    logger.info("Loading data into PostgreSQL")

    df = pd.read_parquet(input_path)

    engine = get_engine()
    
    df.to_sql(
        "sales_staging",
        engine,
        if_exists="replace",
        index=False
    )

    with engine.begin() as conn:

        conn.execute(
            text("""
                INSERT INTO sales
                SELECT *
                FROM sales_staging
                ON CONFLICT (row_id)
                DO UPDATE SET
                sales = EXCLUDED.sales,
                quantity = EXCLUDED.quantity,
                discount = EXCLUDED.discount,
                profit = EXCLUDED.profit;
            """)
        )

    logger.info(f"Loaded {len(df)} rows")