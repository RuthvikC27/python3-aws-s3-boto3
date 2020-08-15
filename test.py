import boto3
from botocore.client import Config
import os
import random
import string

class StorageAWSConfig:
    def __init__(self):
        # S3 Config
        self.AWS_ACCESS_KEY_ID = ""
        self.AWS_SECRET_ACCESS_KEY = ""
        self.AWS_STORAGE_BUCKET_NAME = ""

        self.AWS_S3_FILE_OVERWRITE = False
        self.AWS_DEFAULT_ACL = None
        self.DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    def randomString(self, file=''):
        _, file_extention = os.path.splitext(file)
        file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
        return file_name + file_extention 
        
    def storageDriver(self):
        return boto3.resource(
            's3',
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
            config=Config(signature_version='s3v4')
        )
        

    def uploadFile(self, file):
        
        
        data = open(file, 'rb')

        s3 = self.storageDriver()
        
        # Random name
        uploadFileName = self.randomString(file)
            
        s3.Bucket(self.AWS_STORAGE_BUCKET_NAME).put_object(Key=f'videos/{uploadFileName}', Body=data)
        url = f'https://{self.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{f"videos/{uploadFileName}"}'
        print(url)
        
        return url

    def s3Buckets(self):
        s3 = boto3.resource(
            's3',
            aws_access_key_id=self.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
            config=Config(signature_version='s3v4')
        )
        for bucket in s3.buckets.all():
            print(bucket.name)


    def downloadFile(self, file_to_download):
        s3 = self.storageDriver()
        # Random name
        downloadFileName = self.randomString(file_to_download)

        
        s3.Bucket(self.AWS_STORAGE_BUCKET_NAME).download_file(f'videos/{file_to_download}', f'./{downloadFileName}')

    def readText(self, filename):
        s3 = self.storageDriver()
        
        obj = s3.Object(self.AWS_STORAGE_BUCKET_NAME, f'videos/{filename}')
        body = obj.get()['Body'].read()
        print(body)

storageObj = StorageAWSConfig()

# storageObj.uploadFile('test.jpg')
# storageObj.downloadFile('rueadgklxiimsnqh.jpg')
# storageObj.readText('rueadgklxiimsnqh.jpg')
