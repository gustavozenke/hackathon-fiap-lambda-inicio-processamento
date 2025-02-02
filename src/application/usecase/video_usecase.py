from datetime import datetime

from domain.entitites.video import Video
from infraestructure.repositories.VideoRepositoryImpl import VideoRepositoryImpl


class VideoUsecase:

    def __init__(self):
        self.video_repository = VideoRepositoryImpl()

    def gravar_metadados_video(self, nome_arquivo, nome_usuario, tamanho, formato):
        video = Video(nome_arquivo, nome_usuario, tamanho, formato, str(datetime.now()))
        self.video_repository.gravar_metadados_video(video)
