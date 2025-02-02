import json

import boto3


class SqsUsecase:

    def __init__(self):
        self.sqs_client = boto3.client('sqs')
        self.queue_url = ""

    def send(self, nome_arquivo, nome_usuario):
        message = {
            "nome_arquivo": nome_arquivo,
            "nome_usuario": nome_usuario
        }
        return self.sqs_client.send_message(QueueUrl=self.queue_url, MessageBody=json.dumps(message))
