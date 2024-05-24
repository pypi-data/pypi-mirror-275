import boto3
import os

class S3Client:
    def __init__(self):
        self.service_name = "s3"
        self.access_key = os.getenv("ACCESS_KEY")
        self.secret_key = os.getenv("SECRET_KEY")
        # self.region_name = os.getenv("S3_REGION_NAME")
        self.bucket_name = os.getenv("DOWNLOAD_BUCKET_NAME")


    def upload_file(self, file_name, original_file_name, object_name=None):
        s3_client = boto3.client(
            self.service_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            endpoint_url=os.getenv("ENDPOINT_URL")
        )
        response = s3_client.upload_file(
            file_name,
            self.bucket_name,
            object_name,
            ExtraArgs={
                'ContentDisposition': f'attachment; filename="{original_file_name}"'
            })
        return response
