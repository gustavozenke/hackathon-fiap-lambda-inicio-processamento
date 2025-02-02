from application.usecase.bucket_usecase import BucketUsecase
from application.usecase.sqs_usecase import SqsUsecase
from application.usecase.video_usecase import VideoUsecase


class IniciarProcessamentoService:
    def __init__(self):
        self.bucket_usecase = BucketUsecase()
        self.video_usecase = VideoUsecase()
        self.sqs_usecase = SqsUsecase()

    def iniciar_processamento(self, nome_arquivo, tamanho):
        nome_usuario = nome_arquivo.split('-')[0]
        formato = nome_arquivo.split('.')[1]
        self.video_usecase.gravar_metadados_video(nome_arquivo, nome_usuario, formato, tamanho)
        self.sqs_usecase.send(nome_arquivo, nome_usuario)
