import boto3
from botocore.exceptions import ClientError
from decouple import RepositoryEnv, Config


def init_storage():
    # Load environment variables from .env file
    config = Config(RepositoryEnv(".env"))

    # Initialize the S3 client with AWS credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
        endpoint_url=config('AWS_PUBLIC_STORAGE_ENDPOINT_URL')
    )

    # Specify the bucket names and regions
    public_bucket_name = config('AWS_PUBLIC_STORAGE_BUCKET_NAME')
    private_bucket_name = config('AWS_PRIVATE_STORAGE_BUCKET_NAME')

    # Create the public bucket if it doesn't exist
    try:
        s3.head_bucket(Bucket=public_bucket_name)
        print(f"Bucket '{public_bucket_name}' exists and you have ownership.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"Bucket '{public_bucket_name}' does not exist. Creating the bucket...")
            response1 = s3.create_bucket(Bucket=public_bucket_name)
            print(f"Public Bucket Creation Response: {response1}")
            # If using AWS S3, remove the public access block and update the bucket policy
            if 'amazonaws.com' in config('AWS_PUBLIC_STORAGE_ENDPOINT_URL'):
                try:
                    response2 = s3.delete_public_access_block(Bucket=public_bucket_name)
                    print(f"Public access block removed: {response2}")
                    response3 = s3.put_bucket_policy(
                        Bucket=public_bucket_name,
                        Policy='''{
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Sid": "AllowPublicRead",
                                    "Effect": "Allow",
                                    "Principal": "*",
                                    "Action": "s3:GetObject",
                                    "Resource": "arn:aws:s3:::%s/*"
                                }
                            ]
                        }''' % public_bucket_name
                    )
                    print(f"Bucket policy updated: {response3}")
                except ClientError as e:
                    print(f"Error occurred while updating bucket policy: {e.response['Error']['Message']}")
        else:
            print(f"Error occurred: {e.response['Error']['Message']}")

    # Create the private bucket if it doesn't exist
    try:
        s3.head_bucket(Bucket=private_bucket_name)
        print(f"Bucket '{private_bucket_name}' exists and you have ownership.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"Bucket '{private_bucket_name}' does not exist. Creating the bucket...")
            response1 = s3.create_bucket(Bucket=private_bucket_name)
            print(f"Private Bucket Creation Response: {response1}")
        else:
            print(f"Error occurred: {e.response['Error']['Message']}")
