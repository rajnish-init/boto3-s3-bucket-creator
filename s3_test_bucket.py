import boto3
import botocore.exceptions

region = 'ap-south-1'
bucket_name = 'my-unique-bucket-boto3-rajni-2025'
file_name = 'hello.txt'
object_name = 'devops/hello.txt'

# Step 1: Create S3 client
s3 = boto3.client('s3', region_name=region)

# Step 2: Create Bucket (if not exists)
try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print("✅ Bucket created:", response['Location'])
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        print("ℹ️ Bucket already exists and is owned by you.")
    else:
        print("❌ Error creating bucket:", e)

# Step 3: Upload File
try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"✅ File '{file_name}' uploaded as '{object_name}' in bucket '{bucket_name}'")
except Exception as e:
    print("❌ Upload failed:", e)
