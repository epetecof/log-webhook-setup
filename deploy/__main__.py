import boto3
import os
from datetime import datetime
import json

def main(dict):
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('aws_secret_access_key'),
        aws_secret_access_key=os.environ.get('aws_secret_key_secret'),
        region_name=os.environ.get('aws_secret_region')
    )

    body = dict.get("payload").copy()

    # If necessary, filter Code Engine properties
    # keys = [x for x in list(body.keys()) if "__ce_" in x]
    # for key in keys:
    #     del body[key]

    # Create S3 object key
    object_key = body.get("log_id") + "_" + convert_to_timestamp_str(body.get('request_timestamp'))

    # If necessary, filter specifc keys
    # filter_keys = ['log_id', 'assistant_id', 'response_timestamp']
    # body = {k:body[k] for k in filter_keys if k in body}

    try:
        # Upload JSON file to the S3 bucket
        s3.put_object(
            Bucket=os.environ.get('aws_secret_bucket'),
            Key=object_key+".json",
            Body=(bytes(json.dumps(body).encode('UTF-8'))),
            ContentType='application/json',
        )
        # print(f'JSON uploaded successfully')
    except Exception as e:
        print(f'Erro uploading JSON: {e}')
    
    
    return { 'statusCode': 200, 'body': body}

def convert_to_timestamp_str(date_string):
    date_object = datetime.fromisoformat(date_string)
    
    timestamp = date_object.timestamp()
    return_string = str(timestamp)
    return return_string.replace(".", "-")
    
