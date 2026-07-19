import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine(
    "postgresql://postgres:postgres@postgres-etl:5432/salesdb"
)


def quality_check(input_path):

    df = pd.read_parquet(input_path)

    report = {
        "run_time": datetime.now(),
        "rows": len(df),
        "columns": len(df.columns),
        "missing": int(df.isnull().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "negative_sales": int((df["sales"] < 0).sum()),
        "invalid_quantity": int((df["quantity"] <= 0).sum())
    }

    # -----------------------------
    # Determine Status
    # -----------------------------

    status = "PASS"

    if (
        report["missing"] > 0
        or report["duplicates"] > 0
        or report["negative_sales"] > 0
        or report["invalid_quantity"] > 0
    ):
        status = "FAIL"

    report["status"] = status

    # -----------------------------
    # Print Report
    # -----------------------------

    print("\n========== DATA QUALITY REPORT ==========")

    for key, value in report.items():
        print(f"{key:20}: {value}")

    print("=========================================\n")

    # -----------------------------
    # Save Report
    # -----------------------------

    report_df = pd.DataFrame([report])

    report_df.to_sql(
        "quality_report",
        engine,
        if_exists="append",
        index=False
    )

    # -----------------------------
    # Raise Exception if Failed
    # -----------------------------

    if status == "FAIL":
        raise ValueError("Data Quality Failed")

    print("Data Quality Passed")

    return report