import boto3
import json
from random import uniform
import time
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('AWS_ACCESS_KEY_ID'))
# O ideal, segundo a documentação, seria provisionar uma IAM Role para aplicações efêmeras.
client = boto3.client('kinesis',
    aws_access_key_id = 'AKIAY24ZCR64F2SAOAF3',
    aws_secret_access_key = '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',
    region = 'sa-east-1'
    )

id = 0
while True:
    data = uniform(20, 25)
    id += 1
    input = {
        'idtemp': str(id),
        'data': str(data),
        'type': 'temperature',
        'timestamp': str(datetime.now())
        } 

    client.put_record(
        StreamARN='windfarm',
        Data = json.dumps(input),
        PartitionKey = '02'
    )
    
    time.sleep(10)