from datetime import datetime

from src.domain.entitites.video import Video
from src.infraestructure.video_repository_impl import VideoRepositoryImpl


class VideoUsecase:

    def __init__(self):
        self.video_repository = VideoRepositoryImpl()

    def gravar_metadados_video(self, nome_arquivo):
        video = Video(nome_arquivo, "nome_usuario", "tamanho", "formato", str(datetime.now()))
        self.video_repository.gravar_metadados_video(video)
