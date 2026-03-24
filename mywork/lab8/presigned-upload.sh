#!/bin/bash
# Usage: ./presigned-upload.sh <local_file> <bucket_name> <expires_in_seconds>

LOCAL_FILE=$1
BUCKET=$2
EXPIRES=$3

# Validate arguments
if [ -z "$LOCAL_FILE" ] || [ -z "$BUCKET" ] || [ -z "$EXPIRES" ]; then
  echo "Usage: $0 <local_file> <bucket_name> <expires_in_seconds>"
  exit 1
fi

# Upload the file
echo "Uploading $LOCAL_FILE to s3://$BUCKET/..."
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/"

if [ $? -ne 0 ]; then
  echo "Upload failed."
  exit 1
fi

# Generate presigned URL
echo "Generating presigned URL (expires in $EXPIRES seconds)..."
aws s3 presign --expires-in "$EXPIRES" "s3://$BUCKET/$(basename $LOCAL_FILE)"