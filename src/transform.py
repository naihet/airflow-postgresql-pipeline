import pandas as pd


def transform_data(input_path, output_path):

    df = pd.read_parquet(input_path)

    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["ship_date"] = pd.to_datetime(df["ship_date"])

    df.to_parquet(
        output_path,
        index=False
    )

    return output_path