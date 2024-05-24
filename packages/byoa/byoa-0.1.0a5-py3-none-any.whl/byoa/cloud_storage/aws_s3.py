"""AWS S3 helper functions"""

import os

import boto3
from boto3.exceptions import Boto3Error
from botocore.client import Config


def upload_file(local_file_path: str, bucket_name: str) -> bool:
    """Upload a file to AWS S3 Bucket.

    Args:
      local_file_path(str): The local file path to upload.
      bucket_name(str): The name of the AWS S3 bucket

    Returns:
      bool: True if upload was sucessful, False otherwise

    """

    if bucket_name is None:
        raise ValueError("bucket_name cannot be 'None'")

    s3_client = boto3.client("s3")
    if s3_client and bucket_name is not None:
        try:
            file_name = os.path.basename(local_file_path)
            s3_client.upload_file(local_file_path, bucket_name, file_name)
            return True
        except Boto3Error as error:
            print(f"Error while uploading file to AWS S3: {error}")
            return False
    else:
        return False


def write_folder_to_aws_s3(local_folder_path: str, bucket_name: str) -> bool:
    """Upload a folder to AWS S3 Bucket.

    Args:
      local_folder_path(str): The local folder path to upload
      bucket_name(str): The name of the AWS S3 bucket

    Returns:
      bool: True if upload was sucessful, False otherwise
    """

    if bucket_name is None:
        raise ValueError("bucket_name cannot be 'None'")

    s3_client = boto3.client("s3")
    if s3_client:
        try:
            for root, _, files in os.walk(local_folder_path):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_file_path, local_folder_path)
                    s3_key = os.path.join(
                        os.path.basename(local_folder_path), relative_path
                    ).replace(os.sep, "/")

                    if bucket_name is not None:
                        s3_client.upload_file(local_file_path, bucket_name, s3_key)
            return True
        except Boto3Error as error:
            print(f"Error while uploading folder to AWS S3: {error}")
            return False
    else:
        return False


def get_s3_uri_path(
    local_path: str, bucket_name: str, presigned_url: bool = False, expiration: int = 3600
) -> str:
    """Get the s3 path of the uploaded element (file or folder)

    Args:
      local_path(str): The local path of the uploaded folder/file on s3
      bucket_name(str): The bucket name set to store the file on s3
      presigned_url(bool): Option to presign URL,
      expiration(int): expiration time in second to access presigned urls

    Returns:
      str: the s3 uri of the uploaded folder/file
    """
    # get bucket name
    if bucket_name is None:
        raise ValueError("bucket_name cannot be 'None'")

    s3_key = os.path.basename(local_path)

    # get the region of the bucket to generate presigned url
    region = get_bucket_region(bucket_name)

    s3_client = boto3.client("s3", config=Config(signature_version="s3v4"), region_name=region)
    if presigned_url:
        s3_uri = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": s3_key},
            ExpiresIn=expiration,
            HttpMethod="GET",
        )
        return s3_uri

    return f"s3://{bucket_name}/{s3_key}"


def get_bucket_region(bucket_name):
    """
    Get the region of an S3 bucket.

    Args:
    - bucket_name (str): The name of the S3 bucket.

    Returns:
    - str: The region of the bucket.
    """
    s3 = boto3.client("s3")
    response = s3.get_bucket_location(Bucket=bucket_name)
    region = response.get(
        "LocationConstraint", "us-east-1"
    )  # Default to 'us-east-1' if no location constraint is specified
    return region
