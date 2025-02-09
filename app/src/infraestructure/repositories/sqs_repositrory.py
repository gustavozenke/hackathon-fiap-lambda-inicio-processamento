import json

import boto3

from domain.interfaces.sqs_repository import SqsRepository


class SqsRepositoryImpl(SqsRepository):

    def __init__(self):
        self.sqs_client = boto3.client('sqs', region_name='us-east-1')

    def send(self, message, queue_url):
        return self.sqs_client.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))
