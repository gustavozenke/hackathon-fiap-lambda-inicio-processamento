import json

from src.application.service.iniciar_processamento_service import IniciarProcessamentoService

iniciar_processamento_service = IniciarProcessamentoService()


def lambda_handler(event, context):
    nome_arquivo = event['Records'][0]['s3']['object']['key']
    result = iniciar_processamento_service.iniciar_processamento(nome_arquivo)
    return {'statusCode': 200, 'body': json.dumps(result)}


if __name__ == '__main__':
    event = {
        "Records": [
            {
                "eventVersion": "2.1",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "2025-02-02T18:11:18.417Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {
                    "principalId": "AWS:AROAVMGFHBBMWWOSOTBCW:hackathon-gera-urlpreassinada"
                },
                "requestParameters": {
                    "sourceIPAddress": "187.10.135.221"
                },
                "responseElements": {
                    "x-amz-request-id": "NFWY0SP1N96K90E8",
                    "x-amz-id-2": "KIacnQkzAnILPugqVZxHhcIIdayuXtA3M1Gz8pZpsmO5JV+EHPoO/z9uJby5I3SFqe6mG8KbmQUIKVjaUjWVyQxerc3Tgp4l"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "tf-s3-queue-20250201065941440100000001",
                    "bucket": {
                        "name": "bucket-hackathon-fiap-raw-videos",
                        "ownerIdentity": {
                            "principalId": "A2MD26V13UJX8O"
                        },
                        "arn": "arn:aws:s3:::bucket-hackathon-fiap-raw-videos"
                    },
                    "object": {
                        "key": "gustavozenke-20250202181051.wmv",
                        "size": 11374229,
                        "eTag": "93546134ac3b22a75479dd8325a80c9c",
                        "versionId": "3mMh.8YJwrj9M.NpVUvjq.nQ44lGY1jK",
                        "sequencer": "00679FB5401FC58877"
                    }
                }
            }
        ]
    }
    lambda_handler(event, None)
