#!/usr/bin/env python

import requests
import json
import pandas as pd
import os
import logging
import mysql.connector
from datetime import datetime

# Setup Logging
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"

# Database Configuration (Using env var for password)
# Database Configuration (Pulling from the exports you just did)
# Database Configuration
DB_CONFIG = {
    'host': 'ds2002.cgls84scuy1e.us-east-1.rds.amazonaws.com',
    'user': 'ds2002',
    'database': 'iss',
    'password': os.getenv('DBPASS') # Python is usually better at reading these than Bash
}

def extract(url):
    logging.info(f"Getting data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return None

def register_reporter(table, reporter_id, reporter_name):
    """Checks if reporter exists; if not, inserts them."""
    db = None
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        
        # Check existence
        check_query = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
        cursor.execute(check_query, (reporter_id,))
        
        if cursor.fetchone():
            logging.info(f"Reporter {reporter_id} already registered.")
        else:
            insert_query = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
            logging.info(f"Registered new reporter: {reporter_name}")
            
    except mysql.connector.Error as e:
        logging.error(f"Database error in register_reporter: {e}")
    finally:
        if db and db.is_connected():
            cursor.close()
            db.close()

def load(data, reporter_id):
    """Inserts ISS data into the locations table."""
    db = None
    try:
        # Extract and format values
        message = data.get('message')
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        # Convert Unix timestamp to YYYY-MM-DD HH:MM:SS
        ts = datetime.fromtimestamp(data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')

        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        
        insert_query = """
            INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (message, lat, lon, ts, reporter_id))
        db.commit()
        logging.info(f"Successfully loaded ISS data for {reporter_id} to MySQL")
        
    except Exception as e:
        logging.error(f"Failed to load data to MySQL: {e}")
    finally:
        if db and db.is_connected():
            cursor.close()
            db.close()

def main():
    my_id = 'eby2ch'
    my_name = 'Abdul-Salam Gidado'

    # Step D: Register reporter once
    register_reporter('reporters', my_id, my_name)

    # Step A & C: Extract and Load
    data = extract(URL)
    if data:
        load(data, my_id)

if __name__ == "__main__":
    main()


