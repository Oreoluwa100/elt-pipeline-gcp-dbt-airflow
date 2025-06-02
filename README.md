# elt-pipeline-gcp-dbt-airflow
This project demonstrates how to build an ELT (Extract, Load, Transform) data pipeline for processing daily orders data. The data pipeline simulates order data which mimics real orders, ingests the data into Google Cloud Storage (GCS), loads into BigQuery and transforms the data using dbt, with the whole process being orchestrated by Airflow.

## Overview
**1. Data Simulation:** Generates random order data daily to mimic real-world orders.

**2. Upload to GCS:** The data is stored in a Google Cloud Storage (GCS) bucket.

**3. Load to BigQuery:** Data is loaded from GCS into a staging table in BigQuery.


**4. Transform with DBT:** Data is cleaned, structured into tables, and prepared for reporting and analysis. 

### Technologies Used
- Python: Used to script the data generation [generate_data.py](https://github.com/Oreoluwa100/elt-pipeline-gcp-dbt-airflow/blob/main/ELT_PIPELINE/dags/generate_data.py), data ingestion and loading logic [data_to_gcs_to_bq.py](https://github.com/Oreoluwa100/elt-pipeline-gcp-dbt-airflow/blob/main/ELT_PIPELINE/dags/data_to_gcs_to_bq.py). Also used within the Airflow DAG to orchestrate and execute these Python scripts.

- Apache Airflow: Orchestrates the entire ELT pipeline. It schedules tasks such as data generation, uploading to GCS, loading into BigQuery, and triggering DBT models.

- Google Cloud Storage: Acts as the intermediate storage layer. Simulated JSON order data is first uploaded to a GCS bucket before being moved to BigQuery.

- BigQuery: Serves as the data warehouse where the raw order data is loaded and then transformed using DBT for reporting and analysis.

- DBT (Data Build Tool): Transforms the raw data in BigQuery into structured, analysis-ready datasets using SQL models defined in the project. DBT models are triggered after data is loaded into BigQuery.

- Docker: This is a container for the entire Airflow environment including all dependencies (e.g., DBT, Google Cloud libraries). Ensures that the pipeline runs consistently across environments using docker-compose.

### Prerequisites

1. Docker & Docker Compose
2. GCP Project with BigQuery and GCS API enabled
3. Service account with roles; Storage Admin and Biq Query Admin


