FROM apache/airflow:2.8.1

# Base authentication packages (required for all Google Cloud operations)
RUN pip install --no-cache-dir \
    google-auth \
    google-auth-oauthlib \
    google-auth-httplib2

# Install dependencies
RUN pip install --no-cache-dir \
    apache-airflow-providers-google \
    google-cloud-storage \
    google-cloud-bigquery \
    dbt-core \
    dbt-bigquery

# Copy credentials
COPY config/gcp_credentials.json /opt/airflow/config/

