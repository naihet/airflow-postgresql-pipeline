import pandas as pd


def quality_check(input_path):

    df = pd.read_parquet(input_path)

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "negative_sales": int((df["sales"] < 0).sum()),
        "invalid_quantity": int((df["quantity"] <= 0).sum())
    }

    print("\n========== DATA QUALITY REPORT ==========")

    for key, value in report.items():
        print(f"{key:20}: {value}")

    print("=========================================\n")

    # -----------------------------
    # Validation
    # -----------------------------

    if report["missing"] > 0:
        raise ValueError(
            f"Missing values found ({report['missing']})"
        )

    if report["duplicates"] > 0:
        raise ValueError(
            f"Duplicate rows found ({report['duplicates']})"
        )

    if report["negative_sales"] > 0:
        raise ValueError(
            f"Negative sales found ({report['negative_sales']})"
        )

    if report["invalid_quantity"] > 0:
        raise ValueError(
            f"Invalid quantity found ({report['invalid_quantity']})"
        )

    print("Data Quality Passed")

    return report