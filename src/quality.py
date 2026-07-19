import pandas as pd


def quality_check(input_path):

    df = pd.read_parquet(input_path)

    # -------------------------
    # Missing Values
    # -------------------------

    missing = df.isnull().sum().sum()

    if missing > 0:
        raise ValueError(
            f"Data Quality Failed: {missing} missing values found."
        )

    # -------------------------
    # Duplicate Rows
    # -------------------------

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"Data Quality Failed: {duplicates} duplicate rows found."
        )

    # -------------------------
    # Negative Sales
    # -------------------------

    negative_sales = (df["sales"] < 0).sum()

    if negative_sales > 0:
        raise ValueError(
            f"Data Quality Failed: {negative_sales} negative sales found."
        )

    # -------------------------
    # Quantity <= 0
    # -------------------------

    invalid_quantity = (df["quantity"] <= 0).sum()

    if invalid_quantity > 0:
        raise ValueError(
            f"Data Quality Failed: {invalid_quantity} invalid quantity found."
        )

    print("Data Quality Passed")

    return True