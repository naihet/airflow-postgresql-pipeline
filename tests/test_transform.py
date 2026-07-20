import pandas as pd

from src.transform import transform_data


def test_transform(tmp_path):

    df = pd.DataFrame(
        {
            "Row ID": [1],
            "Order ID": ["CA-001"],
            "Order Date": ["11/8/2016"],
            "Ship Date": ["11/11/2016"],
            "Sales": [100],
            "Quantity": [2],
            "Discount": [0],
            "Profit": [20],
        }
    )

    raw_file = tmp_path / "raw.parquet"
    clean_file = tmp_path / "clean.parquet"

    df.to_parquet(raw_file)

    transform_data(raw_file, clean_file)

    result = pd.read_parquet(clean_file)

    assert "row_id" in result.columns
    assert "order_date" in result.columns