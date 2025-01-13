import json
import boto3
import uuid
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = event['bucket_name']
        file_data = event['file_data']  
        file_name = f"{uuid.uuid4()}.pdf"  
        file_content = bytes(file_data, 'utf-8')

        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content,
            ContentType='application/pdf' 
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully!',
                'file_name': file_name
            })
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error uploading file to S3.',
                'error': str(e)
            })
        }
