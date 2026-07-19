CREATE TABLE IF NOT EXISTS quality_report (

    run_time TIMESTAMP,

    rows INTEGER,

    columns INTEGER,

    missing INTEGER,

    duplicates INTEGER,

    negative_sales INTEGER,

    invalid_quantity INTEGER,

    status VARCHAR(20)

);