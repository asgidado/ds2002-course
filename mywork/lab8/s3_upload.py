import boto3


s3 = boto3.client('s3', region_name='us-east-1')
bucket = 'ds2002-eby2ch'


print("=== Your Buckets ===")
response = s3.list_buckets()
for r in response['Buckets']:
    print(r['Name'])


local_file = 'cloud.jpg'

print(f"\n=== Uploading {local_file} (PRIVATE) ===")
response = s3.put_object(
    Body=open(local_file, 'rb'),   # open in binary read mode
    Bucket=bucket,
    Key=local_file
)
print(f"Status: {response['ResponseMetadata']['HTTPStatusCode']}")
print(f"Test this URL (should get AccessDenied):")
print(f"https://s3.amazonaws.com/{bucket}/{local_file}")


public_file = 'cat.jpg'

print(f"\n=== Uploading {public_file} (PUBLIC) ===")
response = s3.put_object(
    Body=open(public_file, 'rb'),
    Bucket=bucket,
    Key=public_file,
    ACL='public-read'
)
print(f"Status: {response['ResponseMetadata']['HTTPStatusCode']}")
print(f"Test this URL (should load fine):")
print(f"https://s3.amazonaws.com/{bucket}/{public_file}")