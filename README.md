# Airflow ETL Pipeline with PostgreSQL

A Data Engineering project demonstrating a production-style ETL pipeline orchestrated by Apache Airflow. The pipeline extracts sales data from CSV, transforms it with Pandas, stores intermediate data as Parquet, loads data into PostgreSQL through a staging table, performs incremental loading using PostgreSQL `ON CONFLICT`, and validates data quality.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Apache Airflow
- Docker
- Docker Compose

## Project Architecture

```text
CSV
 │
 ▼
Extract
 │
 ▼
raw.parquet
 │
 ▼
Transform
 │
 ▼
clean.parquet
 │
 ▼
PostgreSQL Staging
 │
 ▼
Incremental Load
(ON CONFLICT)
 │
 ▼
PostgreSQL
 │
 ▼
Validation
```

## Features

- Extract sales data from CSV
- Transform data using Pandas
- Store intermediate datasets as Parquet
- Load data into PostgreSQL
- Use a staging table before loading into the production table
- Incremental loading with PostgreSQL `ON CONFLICT`
- Prevent duplicate records using Primary Key
- Validate dataset quality
- Dynamic file paths using Airflow XCom
- Schedule ETL workflow using Apache Airflow
- Containerized development environment with Docker Compose

## Project Structure

```text
.
├── dags/
├── src/
├── data/
├── temp/
├── logs/
├── config/
├── plugins/
├── sql/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Airflow Workflow

```text
Extract
   │
   │ (XCom)
   ▼
Transform
   │
   │ (XCom)
   ▼
Load
   │
   ▼
Validate
```

## Docker Services

- Airflow API Server
- Airflow Scheduler
- Airflow Worker
- Airflow Triggerer
- Airflow DAG Processor
- Redis
- PostgreSQL (Airflow Metadata Database)
- PostgreSQL (ETL Database)

## Learning Outcomes

- ETL Pipeline Design
- Apache Airflow DAG
- Airflow XCom
- PythonOperator
- PostgreSQL Integration
- SQLAlchemy
- Staging Table Design
- Incremental ETL
- PostgreSQL `ON CONFLICT`
- Data Validation
- Docker Compose Multi-Container Architecture
- Workflow Orchestration

## Future Improvements

- Incremental ETL with `ON CONFLICT DO UPDATE`
- Data Quality Rules
- AWS S3 / MinIO Integration
- dbt for Data Transformation
- Spark / PySpark Integration
- Monitoring and Alerting