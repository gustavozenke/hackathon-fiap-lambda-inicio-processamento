import logging
import os

from domain.entitites.video import Video
from domain.interfaces.envio_processamento import EnvioProcessamento
from domain.interfaces.sqs_repository import SqsRepository

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class EnvioProcessamentoUseCase(EnvioProcessamento):
    def __init__(self, sqs_repository: SqsRepository):
        self.sqs_repository = sqs_repository
        self.queue_processamento_url = os.getenv("QUEUE_PROCESSAMENTO_URL")

    def iniciar_processamento(self, video: Video):
        logger.info(f"Enviando video {video.nome_video} para inicio de processamento")
        payload = {
            "nome_video": video.nome_video,
            "nome_usuario": video.nome_usuario
        }
        response = self.sqs_repository.send(payload, self.queue_processamento_url)
        logger.info(f"Video {video.nome_video} enviado para inicio de processamento com sucesso. Response={response}")
