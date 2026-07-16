# Airflow ETL Pipeline with PostgreSQL

A simple Data Engineering project demonstrating an ETL pipeline orchestrated by Apache Airflow. The pipeline extracts sales data from CSV, transforms it using Pandas, loads it into PostgreSQL, and performs basic data validation.

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
Transform
 │
 ▼
Load
 │
 ▼
PostgreSQL
 │
 ▼
Validation
```

## Features

- Extract sales data from CSV
- Transform dataset with Pandas
- Load data into PostgreSQL
- Validate dataset quality
- Schedule ETL workflow using Apache Airflow
- Containerized environment with Docker Compose

## Project Structure

```
.
├── dags/
├── src/
├── data/
├── logs/
├── config/
├── plugins/
├── sql/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Airflow Workflow

```
Extract
   │
   ▼
Transform
   │
   ▼
Load
   │
   ▼
Validate
```

## Docker Services

- Airflow Webserver (API Server)
- Airflow Scheduler
- Airflow Worker
- Airflow Triggerer
- Airflow DAG Processor
- Redis
- PostgreSQL (Airflow Metadata)
- PostgreSQL (ETL Database)

## Learning Outcomes

- Apache Airflow DAG
- PythonOperator
- Docker Compose Multi-Container
- PostgreSQL Integration
- SQLAlchemy
- ETL Pipeline Design
- Workflow Orchestration