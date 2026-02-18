#!/usr/bin/env python

import requests
import json
import pandas as pd
import os
import sys
import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"

def extract(url):
    """
    Extract: Downloads the JSON data from the API endpoint and returns the parsed JSON data record.
    Handles errors gracefully using try/except blocks.
    """
    logging.info(f"Getting data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        logging.info("Data successfully extracted from API")
        return data
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"A request error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return None

def transform(data):
    """
    Transform: Converts the JSON data record into a tabular format with pandas.
    Converts the timestamp into a more intuitive format (YYYY-MM-DD HH:MM:SS).
    Returns the tabularized record as a pandas DataFrame.
    """
    try:
        timestamp = data['timestamp']
        position = data['iss_position']

        datetime = pd.to_datetime(timestamp, unit='s')

        df = pd.DataFrame({
            'timestamp': [datetime.strftime('%Y-%m-%d %H:%M:%S')],
            'latitude': [position['latitude']],
            'longitude': [position['longitude']]
        })

        logging.info("Transformed data into DataFrame")
        return df
    except KeyError as e:
        logging.error(f"Key error occurred while transforming data: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while transforming data: {e}")
    return None

def load(df, csv_file):
    """
    Load: Appends the tabularized data record to the specified CSV file.
    Creates the file if it does not exist.
    """
    try:
        if os.path.exists(csv_file):
            existing_data = pd.read_csv(csv_file)
            df = pd.concat([existing_data, df], ignore_index=True)
        df.to_csv(csv_file, index=False)
        logging.info(f"Loaded transformed data (saved to {csv_file})")
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")

def main():
    """
    Main: Orchestrates the ETL process by calling extract, transform, and load functions in sequence.
    """
    json_file = "iss_data.json"  # Temporary file to save raw JSON
    csv_file = "iss_data.csv"   # Output CSV file

    # Extract
    data = extract(URL)
    if data is None:
        logging.error("Extraction failed. Exiting.")
        return

    # Transform
    df = transform(data)
    if df is None:
        logging.error("Transformation failed. Exiting.")
        return

    # Load
    load(df, csv_file)

if __name__ == "__main__":
    main()