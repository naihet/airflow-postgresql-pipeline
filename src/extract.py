import pandas as pd


def extract_data(csv_path, output_path):

    df = pd.read_csv(
        csv_path,
        encoding="latin1"
    )

    df.to_parquet(
        output_path,
        index=False
    )

    return output_path