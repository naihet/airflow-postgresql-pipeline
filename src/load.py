import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine(
    "postgresql://postgres:postgres@postgres-etl:5432/salesdb"
)


def load_data(input_path):

    df = pd.read_parquet(input_path)

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