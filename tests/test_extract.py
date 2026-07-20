from pathlib import Path

from src.extract import extract_data


def test_extract(tmp_path):

    output = tmp_path / "raw.parquet"

    result = extract_data(
        "data/Sample - Superstore.csv",
        output
    )

    assert Path(result).exists()