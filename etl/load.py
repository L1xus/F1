from dotenv import load_dotenv
import boto3
import json
import os

load_dotenv()
aws_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')

def load_data(data, bucket_name, file_name):
    # Convertir le dictionnaire en JSON, puis encoder en UTF-8
    result_json = json.dumps(data, indent=4)
    result_bytes = result_json.encode('utf-8')

    # Configuration S3
    # bucket_name = "f1-aws"
    # s3_key = "data/result.json"

    # Initialiser le client S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret,
        region_name='eu-west-3'
    )

    try:
        s3.put_object(Body=result_bytes, Bucket=bucket_name, Key=file_name)
        print(f"Fichier chargé avec succès dans S3 : s3://{bucket_name}/{file_name}")
    except Exception as e:
        print(f"Erreur lors du chargement vers S3 : {e}")
