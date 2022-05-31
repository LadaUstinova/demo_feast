import boto3

client = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net/',
    aws_access_key_id = 'OGUruVnslHlArHK5aCrs',
    aws_secret_access_key = '4qBhtOZHVES-3NqEe-bErGPxWaZwIrQRUUk6v9jn')

for key in client.list_objects(Bucket='rnd-feast')['Contents']:
    print(key['Key'])