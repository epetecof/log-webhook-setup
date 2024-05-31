import boto3
import os
from datetime import datetime
import json

def main(dict):
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('aws_secret_access_key'),
        aws_secret_access_key=os.environ.get('aws_secret_key_secret'),
        region_name=os.environ.get('aws_secret_region')  # substitua pela região de sua preferência
    )

    body = dict.get("payload").copy()

    # keys = [x for x in list(body.keys()) if "__ce_" in x]
    # for key in keys:
    #     del body[key]

    object_key = body.get("log_id") + "_" + convert_to_timestamp_str(body.get('request_timestamp'))
    # body['object_key'] = object_key

    # filter_keys = ['log_id', 'assistant_id', 'response_timestamp']
    # body = {k:body[k] for k in filter_keys if k in body}

    try:
        # Faça o upload do arquivo JSON para o bucket S3
        s3.put_object(
            Bucket=os.environ.get('aws_secret_bucket'),
            Key=object_key+".json",
            Body=(bytes(json.dumps(body).encode('UTF-8'))),
            ContentType='application/json',
        )
        print(f'Arquivo JSON subido com sucesso.')
    except Exception as e:
        print(f'Erro ao subir arquivo JSON: {e}')
    
    
    return { 'statusCode': 200, 'body': body}

def convert_to_timestamp_str(date_string):
    # Converter a string em um objeto datetime
    date_object = datetime.fromisoformat(date_string)

    # Converter o objeto datetime em um timestamp
    timestamp = date_object.timestamp()
    return_string = str(timestamp)
    return return_string.replace(".", "-")
    
