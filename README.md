# Airflow ETL Pipeline with PostgreSQL

[![Python Tests](https://github.com/naihet/airflow-postgresql-pipeline/actions/workflows/python-tests.yml/badge.svg)](https://github.com/naihet/airflow-postgresql-pipeline/actions/workflows/python-tests.yml)

A Data Engineering project demonstrating a production-style ETL pipeline orchestrated by Apache Airflow. The pipeline extracts sales data from CSV, transforms it with Pandas, stores intermediate data as Parquet, loads data into PostgreSQL through a staging table, performs incremental loading using PostgreSQL `ON CONFLICT`, and validates data quality.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Apache Airflow
- Docker
- Docker Compose
- Pytest
- Discord Webhook

## Project Architecture

```text
                    +----------------+
                    |  CSV Dataset   |
                    +----------------+
                             │
                             ▼
                      Extract (CSV)
                             │
                             ▼
                      raw.parquet
                             │
                             ▼
                     Transform Data
                             │
                             ▼
                     clean.parquet
                             │
                             ▼
                    Data Quality Check
                             │
                     PASS / FAIL
                             │
             ┌───────────────┴───────────────┐
             │                               │
             ▼                               ▼
      Discord Alert                    Stop Pipeline
             │
             ▼
       PostgreSQL Staging
             │
             ▼
 Incremental Load (ON CONFLICT)
             │
             ▼
        PostgreSQL Sales DB
             │
             ▼
        Validation Report
             │
             ▼
      Discord Success Alert
```

## Features

- Extract sales data from CSV
- Transform data using Pandas
- Store intermediate datasets as Parquet
- Dynamic file paths using Airflow XCom
- Data Quality validation
- Production-style logging
- Incremental loading using PostgreSQL ON CONFLICT
- Staging table architecture
- Prevent duplicate records using Primary Key
- Discord notifications for pipeline success and failure
- Unit testing with Pytest
- Apache Airflow DAG orchestration
- Containerized development environment using Docker Compose

## Project Structure

```text
.
├── dags/
├── src/
├── tests/
├── data/
├── temp/
├── logs/
├── config/
├── plugins/
├── sql/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pytest.ini
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
Quality Check
   │
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

## Testing

Unit tests are implemented using Pytest.

Current test coverage includes:

- Extract module
- Transform module

Run all tests:

`docker compose exec airflow-apiserver pytest -v`

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
- Data Quality Validation
- Production Logging
- Discord Webhook Integration
- Unit Testing with Pytest
- Docker Compose Multi-Container Architecture
- Workflow Orchestration

## Future Improvements

- Increase Unit Test Coverage
- GitHub Actions CI/CD
- Airflow Connections & Variables
- AWS S3 / MinIO Integration
- dbt for Data Transformation
- Spark / PySpark Integration
- Monitoring and Alerting