import boto3

def create_s3_bucket(bucket_name, aws_region):
    # Create an S3 client
    s3_client = boto3.client('s3')

    # Create the S3 bucket
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': aws_region
            }
        )
        print(f"S3 bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python create_s3_bucket.py <bucket_name> <aws_region>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    aws_region = sys.argv[2]
    create_s3_bucket(bucket_name, aws_region)
