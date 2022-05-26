import json
import boto3

bucket_name = "coop-odometer"
region = "us-east-1"

def lambda_handler(event, context):
    
    file_name = event['queryStringParameters']['key']
    textract_client = boto3.client('textract', region_name=region)
    response = textract_client.analyze_id(DocumentPages=[{"S3Object":{"Bucket":bucket_name,"Name":file_name}}])
    result = []
    
    for doc_fields in response['IdentityDocuments']:
        for id_field in doc_fields['IdentityDocumentFields']:
            result.append(id_field)
            
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }