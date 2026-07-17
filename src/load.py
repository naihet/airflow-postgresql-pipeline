import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgres@postgres-etl:5432/salesdb"
)


def load_data(input_path):

    df = pd.read_parquet(input_path)

    df.to_sql(
        "sales",
        engine,
        if_exists="replace",
        index=False
    )