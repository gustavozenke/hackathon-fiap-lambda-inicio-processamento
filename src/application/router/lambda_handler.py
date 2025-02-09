import json
import logging

from application.usecase.envio_processamento_usecase import EnvioProcessamentoUseCase
from application.service.iniciar_processamento_service import IniciarProcessamentoService
from infraestructure.repositories.sqs_repositrory import SqsRepositoryImpl
from application.usecase.gravar_video_usecase import GravarVideoUseCase
from infraestructure.repositories.Video_repository_impl import VideoRepositoryImpl

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    sqs_repository = SqsRepositoryImpl()
    enviar_processamento_usecase = EnvioProcessamentoUseCase(sqs_repository)
    video_repository = VideoRepositoryImpl()
    video_usecase = GravarVideoUseCase(video_repository)
    iniciar_processamento_service = IniciarProcessamentoService(video_usecase, enviar_processamento_usecase)

    logger.info(f"Mensagem recebida={event}")

    body = json.loads(event['Records'][0]['body'])
    nome_video = body['Records'][0]['s3']['object']['key']
    tamanho = body['Records'][0]['s3']['object']['size']

    iniciar_processamento_service.execute(nome_video, tamanho)

    response = {'statusCode': 200, 'body': 'Mensagem processada com sucesso!'}
    logger.info(response)
    return response



if __name__ == '__main__':
    event = {
        "Records": [{
            "body": '{"Records":[{"eventVersion":"2.1","eventSource":"aws:s3","awsRegion":"us-east-1","eventTime":"2025-02-02T20:57:06.892Z","eventName":"ObjectCreated:Put","userIdentity":{"principalId":"AWS:AROAVMGFHBBMWWOSOTBCW:hackathon-gera-urlpreassinada"},"requestParameters":{"sourceIPAddress":"187.10.135.221"},"responseElements":{"x-amz-request-id":"N1WRNMMGGY601FW5","x-amz-id-2":"wIbejgJPphg9EJVTII/rVaSiTpaseA2sZdJc5yVj5N5O85dAn5aq3WvQtO32+f+PYLPmrMCLFslsxwb5Mjunb24ZPq8W7WZ+"},"s3":{"s3SchemaVersion":"1.0","configurationId":"tf-s3-queue-20250201065941440100000001","bucket":{"name":"bucket-hackathon-fiap-raw-videos","ownerIdentity":{"principalId":"A2MD26V13UJX8O"},"arn":"arn:aws:s3:::bucket-hackathon-fiap-raw-videos"},"object":{"key":"gustavozenke-20250202205623.wmv","size":11374229,"eTag":"93546134ac3b22a75479dd8325a80c9c","versionId":"CIiz9Y_P57ZdsYKBCJ19sMO2Qre2hrwk","sequencer":"00679FDC1C9323CC77"}}}]}',
        }]
    }

    lambda_handler(event, None)
