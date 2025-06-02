"""
This script ingests the order data, uploads it to Google Cloud Storage (GCS),
and then loads it into BigQuery. It uses Google Cloud libraries and credentials 
configured in a JSON key file.
"""

def data_gcs_bq():
    import json
    import os
    from datetime import datetime, timedelta, time

    from generate_data import generate_order

    from google.oauth2 import service_account
    from google.cloud import storage
    from google.cloud import bigquery

    # Load GCP credentials from the airflow container environment variable
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv('GCP_CREDENTIALS_PATH', '/opt/airflow/config/gcp_credentials.json')
    )

    # Upload simulated data to GCS
    def upload_to_gcs(bucket_name, data, filename):
        client = storage.Client(credentials=credentials)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(f"orders/{filename}")
        blob.upload_from_string(data)

    # Upload data from GCS to BigQuery
    def gcs_to_bq(bucket_name, file_name):
        client = bigquery.Client(credentials=credentials)

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect=True,
            write_disposition="WRITE_APPEND"
        )

        uri = f"gs://{bucket_name}/orders/{file_name}"
        table_id = "credible-skill-453411-c1.staging_dataset.raw_orders"

        load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()

    bucket_name = "oreoluwa_bucket001"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"orders_{timestamp}.json"

    # Simulate 100 orders
    orders = [generate_order() for _ in range(100)]
    json_data = "\n".join(json.dumps(order) for order in orders)

    # Upload to GCS and load into BigQuery
    upload_to_gcs(bucket_name, json_data, file_name)
    gcs_to_bq(bucket_name, file_name)

    print(f"Successfully uploaded orders data to gs://{bucket_name}/orders/{file_name} and loaded into BigQuery.")

