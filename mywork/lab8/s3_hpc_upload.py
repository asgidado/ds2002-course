#!/usr/bin/env python3
"""
s3_hpc_upload.py

Uploads result CSV files from a local/HPC folder to an AWS S3 bucket.

Usage:
    python3 s3_hpc_upload.py <input_folder> <bucket/prefix>

Example:
    python3 s3_hpc_upload.py /scratch/$USER/ds2002-jobruns/text-analysis ds2002-eby2ch/book-analysis/
"""

import argparse
import boto3
import glob
import logging
import os
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)



def parse_args():
    """
    Parse command line arguments.

    Returns:
        tuple: (input_folder, destination)
            - input_folder (str): Path to the local folder containing results*.csv files.
            - destination  (str): S3 destination in the format 'bucket-name/prefix/'.
    """
    parser = argparse.ArgumentParser(
        description="Upload results CSV files from an HPC scratch folder to AWS S3."
    )
    parser.add_argument(
        "input_folder",
        help="Path to the folder containing results*.csv files (e.g. /scratch/$USER/ds2002-jobruns/text-analysis)"
    )
    parser.add_argument(
        "destination",
        help="S3 bucket and prefix to upload to (e.g. ds2002-eby2ch/book-analysis/)"
    )

    args = parser.parse_args()
    return args.input_folder, args.destination



def upload(input_folder, destination):
    """
    Upload all results*.csv files from input_folder to an S3 bucket/prefix.

    Args:
        input_folder (str): Local directory containing the CSV files to upload.
        destination  (str): S3 destination string in 'bucket-name/prefix/' format.

    Returns:
        bool: True if all files uploaded successfully, False if any error occurred.
    """
    # Split destination into bucket name and prefix
    parts = destination.strip("/").split("/", 1)
    bucket = parts[0]
    prefix = parts[1] + "/" if len(parts) > 1 else ""

    # Find all matching CSV files
    pattern = os.path.join(input_folder, "results*.csv")
    files = sorted(glob.glob(pattern))

    if not files:
        logger.warning(f"No files matching 'results*.csv' found in: {input_folder}")
        return False

    logger.info(f"Found {len(files)} file(s) to upload → s3://{bucket}/{prefix}")

    try:
        s3 = boto3.client("s3", region_name="us-east-1")

        for filepath in files:
            filename = os.path.basename(filepath)
            s3_key = prefix + filename

            logger.info(f"Uploading {filename} → s3://{bucket}/{s3_key}")

            with open(filepath, "rb") as f:
                s3.put_object(
                    Body=f,
                    Bucket=bucket,
                    Key=s3_key
                )

        return True

    except Exception as e:
        logger.error(f"Upload failed: {e}")
        return False



def main():
    """
    Main entry point. Parses arguments, runs the upload, and logs the outcome.
    """
    input_folder, destination = parse_args()

    logger.info(f"Starting upload from '{input_folder}' to '{destination}'")
    success = upload(input_folder, destination)

    if success:
        logger.info("✓ All files uploaded successfully.")
    else:
        logger.error("✗ Upload completed with errors. Check logs above.")
        sys.exit(1)



if __name__ == "__main__":
    main()