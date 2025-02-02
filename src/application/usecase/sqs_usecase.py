import json

import boto3


class SqsUsecase:

    def __init__(self):
        self.sqs_client = boto3.client('sqs')

    def send(self, message, queue_url):
        return self.sqs_client.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))
