import logging
from datetime import datetime

import pytz

from domain.entitites.video import Video
from domain.interfaces.envio_processamento import EnvioProcessamento
from domain.interfaces.iniciar_processamento import IniciarProcessamento
from domain.interfaces.gravar_video import GravarVideo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tz_br = pytz.timezone("America/Sao_Paulo")


class IniciarProcessamentoService(IniciarProcessamento):
    def __init__(self, gravar_video_usecase: GravarVideo, enviar_processamento_usecase: EnvioProcessamento):
        self.gravar_video_usecase = gravar_video_usecase
        self.enviar_processamento_usecase = enviar_processamento_usecase

    def execute(self, nome_video, tamanho):
        try:
            nome_usuario = nome_video.split('-')[0]
            formato = nome_video.split('.')[1]
            data_hora = str(datetime.now().astimezone(tz_br))

            video = Video(nome_video, nome_usuario, tamanho, formato, data_hora)

            self.gravar_video_usecase.gravar_metadados_video(video)
            self.enviar_processamento_usecase.iniciar_processamento(video)
        except Exception as erro:
            logger.error(f"Erro ao processar mensagem. Erro={erro.args}")
            raise erro
