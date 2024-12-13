from dotenv import load_dotenv
import boto3
import csv
import os

load_dotenv()
aws_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')


def load_data(data, bucket_name, file_name):
    # Validate that data is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")

    csv_file_path = "/tmp/temp_data.csv"
    try:
        # Extract all unique headers dynamically
        headers = {"key"}
        for value in data.values():
            if isinstance(value, dict):
                headers.update(value.keys())
            elif isinstance(value, (int, float, str)):
                headers.add("value")
        
        headers = list(headers)

        # Write data to a temporary CSV file
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            for key, value in data.items():
                if isinstance(value, dict):
                    row = {"key": key, **value}
                else:
                    row = {"key": key, "value": value}
                writer.writerow(row)

        # Read the CSV file as bytes
        with open(csv_file_path, 'rb') as f:
            csv_bytes = f.read()

    except Exception as e:
        print(f"Erreur lors de la création du fichier CSV : {e}")
        return

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret,
        region_name='eu-west-3'
    )

    try:
        # Upload the CSV file content to S3
        s3.put_object(Body=csv_bytes, Bucket=bucket_name, Key=file_name)
        print(f"CSV file saved succesfully into S3 : s3://{bucket_name}/{file_name}")
    except Exception as e:
        print(f"Erreur while saving to S3 : {e}")
