import logging

from domain.entitites.video import Video
from domain.interfaces.video_repository import VideoRepository
from domain.interfaces.gravar_video import GravarVideo

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


class GravarVideoUseCase(GravarVideo):

    def __init__(self, video_repository: VideoRepository):
        self.video_repository = video_repository

    def gravar_metadados_video(self, video: Video):
        payload = {
                'nome_usuario': video.nome_usuario,
                'nome_video': video.nome_video,
                'tamanho': video.tamanho,
                'formato': video.formato,
                'data_hora_inclusao': video.data_hora_inclusao
            }

        logger.info(f"Gravando metadados do video {video.nome_video}. Metadados={payload}")

        response = self.video_repository.put_item(payload)

        logger.info(f"Metadados do video {video.nome_video} persistidos com sucesso. Response={response}")
