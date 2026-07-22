import boto3

client = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
)


def upload_file(local_path, bucket_name, object_name):

    client.upload_file(
        local_path,
        bucket_name,
        object_name,
    )

    print(f"Uploaded {object_name} to {bucket_name}")

def download_file(bucket_name, object_name, local_path):

    client.download_file(
        bucket_name,
        object_name,
        local_path
    )

    print(f"Downloaded {object_name}")