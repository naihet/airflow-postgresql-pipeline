def validate_data(df):

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": df.duplicated().sum(),
        "missing": df.isnull().sum().to_dict()
    }