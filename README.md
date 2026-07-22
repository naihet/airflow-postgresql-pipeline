# Airflow ETL Pipeline with PostgreSQL

[![Python Tests](https://github.com/naihet/airflow-postgresql-pipeline/actions/workflows/python-tests.yml/badge.svg)](https://github.com/naihet/airflow-postgresql-pipeline/actions/workflows/python-tests.yml)

A production-style Data Engineering project demonstrating an end-to-end ETL pipeline orchestrated by Apache Airflow. The pipeline uploads source data to MinIO (S3-compatible object storage), downloads it for processing, transforms data with Pandas, performs data quality validation, incrementally loads records into PostgreSQL, and sends Discord notifications for both success and failure events.

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Apache Airflow
- MinIO (S3 Compatible Object Storage)
- Docker
- Docker Compose
- GitHub Actions
- Pytest
- Discord Webhook

---

## Project Architecture

```text
                    +----------------+
                    |   CSV Dataset  |
                    +----------------+
                             │
                             ▼
                   Upload to MinIO (S3)
                             │
                             ▼
                   Download from MinIO
                             │
                             ▼
                      Extract (CSV)
                             │
                             ▼
                    raw.parquet (Temp)
                             │
                             ▼
                    Transform Data
                             │
                             ▼
                   clean.parquet (Temp)
                             │
                             ▼
                  Data Quality Validation
                             │
                   PASS              FAIL
                     │                │
                     ▼                ▼
             PostgreSQL Staging   Discord Alert
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
          Cleanup Temporary Files
                     │
                     ▼
         Discord Success Notification
```

---

## Features

- Upload source files to MinIO (S3-compatible storage)
- Download datasets from MinIO before processing
- Extract sales data from CSV
- Transform data using Pandas
- Store intermediate datasets as Parquet
- Dynamic file paths using Airflow XCom
- Data Quality validation
- Production-style logging
- Cleanup temporary files after successful execution
- Incremental loading using PostgreSQL `ON CONFLICT`
- Staging table architecture
- Prevent duplicate records using Primary Key
- Discord notifications for pipeline success and failure
- Unit testing with Pytest
- GitHub Actions Continuous Integration
- Apache Airflow DAG orchestration
- Containerized development environment using Docker Compose

---

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
├── .github/
│   └── workflows/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Airflow Workflow

```text
Upload
   │
   ▼
Download
   │
   │ (XCom)
   ▼
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
   │
   ▼
Cleanup
```

---

## Docker Services

- Airflow API Server
- Airflow Scheduler
- Airflow Worker
- Airflow Triggerer
- Airflow DAG Processor
- Redis
- PostgreSQL (Airflow Metadata Database)
- PostgreSQL (ETL Database)
- MinIO (Object Storage)

---

## Testing

Unit tests are implemented using Pytest.

Current test coverage includes:

- Extract module
- Transform module

Run all tests:

```bash
docker compose exec airflow-apiserver pytest -v
```

---

## CI

GitHub Actions automatically executes unit tests on every push and pull request.

Current workflow:

- Install dependencies
- Run Pytest
- Report build status

---

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
- Object Storage (MinIO / S3)
- Data Quality Validation
- Production Logging
- Discord Webhook Integration
- Unit Testing with Pytest
- GitHub Actions CI
- Docker Compose Multi-Container Architecture
- Workflow Orchestration

---

## Future Improvements

- Increase Unit Test Coverage
- Airflow Connections & Variables
- AWS S3 Migration
- dbt for Data Transformation
- Spark / PySpark Integration
- Data Lineage
- Monitoring Dashboard (Prometheus + Grafana)