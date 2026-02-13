#!/usr/bin/env python

import requests
import json
import pandas as pd
import sys
import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"
csv_file = sys.argv[1]

def extract(url, json_file): 
    """
    Extract: Get data from API and save raw JSON.
    Returns the number of records in the raw data.
    """
    logging.info(f"Getting data from {url}")

    try:
        response = requests.get(url)
        response.raise_for_status() # raise an exception for HTTP errors
        data = response.json()
        
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        logging.info(f"Extracted raw data and saved to {json_file}")
    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
        logging.error("A request error occurred:", e)
    except Exception as e:
        logging.error("An unexpected error occurred:", e)

def transform(json_file):
    """
    Transform: Load raw JSON, flatten, and keep only selected fields.
    Returns a cleaned DataFrame.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        timestamp = data['timestamp']
        position = data['iss_position']

        datetime = pd.to_datetime(timestamp, unit='s')

        df = pd.DataFrame({
            'timestamp': datetime.strfttime('%Y-%m-%d %H:%M:%S'),
            'latitude': [position['latitude']],
            'longitude': [position['longitude']]
        })

        logging.info("Transformed data into DataFrame")
        return df
    except KeyError as e:
        logging.error("Key error occurred while transforming data:", e)
    except Exception as e:
        logging.error("An unexpected error occurred while transforming data:", e)


if __name__ == "__main__":
    main()