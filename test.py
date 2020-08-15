import boto3
from botocore.client import Config

# S3 Config

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_STORAGE_BUCKET_NAME = ""


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

data = open('test.jpg', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version='s3v4')
)

# for bucket in s3.buckets.all():
#     print(bucket.name)

# Upload file
file_upload = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key='images/test1.jpg', Body=data)
url = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{"images/test1.jpg"}'
# print(file_upload)
print(url)

# Download
s3.Bucket(AWS_STORAGE_BUCKET_NAME).download_file('images/test1.jpg', './bitmoji.png')

# Read text
obj = s3.Object(AWS_STORAGE_BUCKET_NAME, 'images/test1.jpg')
body = obj.get()['Body'].read()
print(body)

