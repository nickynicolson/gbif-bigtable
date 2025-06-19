This repo demonstrates how you can access GBIF data via SQL against a Google BigQuery table

## Background

GBIF mediated occurrence data is available in a Google BigQuery table, which allows you to run SQL queries against the data. This can be useful for data analysis, visualization, and integration with other datasets.
See the GBIF documentation on data presence in cloud computing services at https://techdocs.gbif.org/en/cloud-services/

## Setup

1. Install google-cloud-sdk
    - Follow the instructions at https://cloud.google.com/sdk/docs/install
1. Set up Google Cloud credentials using the gcloud CLI
    ```bash
    gcloud auth application-default login
    ```
1. Setup a virtual environment (optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
1. Install client libraries
    ```bash
    pip install --upgrade pandas-gbq 'google-cloud-bigquery[bqstorage,pandas]'
    ```
1. Run the python script
    ```bash
    python gbif_bigtable_query.py
    ```