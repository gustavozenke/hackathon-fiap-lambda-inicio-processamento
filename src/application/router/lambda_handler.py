import json

from application.service.iniciar_processamento_service import IniciarProcessamentoService

iniciar_processamento_service = IniciarProcessamentoService()


def lambda_handler(event, context):
    body = json.loads(event['Records'][0]['body'])
    nome_video = body['Records'][0]['s3']['object']['key']
    tamanho = body['Records'][0]['s3']['object']['size']
    result = iniciar_processamento_service.iniciar_processamento(nome_video, tamanho)
    return {'statusCode': 200, 'body': json.dumps(result)}


if __name__ == '__main__':
    event = {
        "Records": [
            {
                "messageId": "0c5747e3-52dd-43b9-8a64-e671a99d4de2",
                "receiptHandle": "AQEBNLxg2VKvjWYBXrXlR2sA5IZfVvDPdMsmXysDAy4FZ+3pA8ly4mICNAILFgiaBasL0ugczK1uOCTyVxlfcYj4ToMXebvTGjCgmQRYyzjEa5EclQRLzI96qiLfD+d/Lgl/oofWI4TEbnigOOtWjE60eqA63KBfaMQgVzqyqnRymzg2lzasL4GkbHWkCqctHyvR0Z89euMGaEBM+WEhHXNZp73YWdobb4qoX6/6BWtX5EpbOyuW7GAODLQQNhLj7nigvkEjlV/NWVv+hY2YPx0dtWe2BmkB0wQ88W3UVAzDIbFBlzHhZ/UxrnxJlEfYhMEvnHjwwlnsw1yP4zDFG3sX11ophF+eJaoTPAR6/k8Dn9sTcCTiVB39l7BpzXZ5MGJrdlzd9qYo3nRHTnVRkZoWwg==",
                "body": '{"Records":[{"eventVersion":"2.1","eventSource":"aws:s3","awsRegion":"us-east-1","eventTime":"2025-02-02T20:57:06.892Z","eventName":"ObjectCreated:Put","userIdentity":{"principalId":"AWS:AROAVMGFHBBMWWOSOTBCW:hackathon-gera-urlpreassinada"},"requestParameters":{"sourceIPAddress":"187.10.135.221"},"responseElements":{"x-amz-request-id":"N1WRNMMGGY601FW5","x-amz-id-2":"wIbejgJPphg9EJVTII/rVaSiTpaseA2sZdJc5yVj5N5O85dAn5aq3WvQtO32+f+PYLPmrMCLFslsxwb5Mjunb24ZPq8W7WZ+"},"s3":{"s3SchemaVersion":"1.0","configurationId":"tf-s3-queue-20250201065941440100000001","bucket":{"name":"bucket-hackathon-fiap-raw-videos","ownerIdentity":{"principalId":"A2MD26V13UJX8O"},"arn":"arn:aws:s3:::bucket-hackathon-fiap-raw-videos"},"object":{"key":"gustavozenke-20250202205623.wmv","size":11374229,"eTag":"93546134ac3b22a75479dd8325a80c9c","versionId":"CIiz9Y_P57ZdsYKBCJ19sMO2Qre2hrwk","sequencer":"00679FDC1C9323CC77"}}}]}',
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1738529827486",
                    "SenderId": "AROA4R74ZO52XAB5OD7T4:S3-PROD-END",
                    "ApproximateFirstReceiveTimestamp": "1738529827497",
                },
                "messageAttributes": {},
                "md5OfBody": "df84c047abd336dca724f7e87b7f68f8",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:369780787289:sqs-inicio-processamento",
                "awsRegion": "us-east-1",
            }
        ]
    }

    lambda_handler(event, None)
