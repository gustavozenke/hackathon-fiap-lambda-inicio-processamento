from application.usecase.bucket_usecase import BucketUsecase
from application.usecase.sqs_usecase import SqsUsecase
from application.usecase.video_usecase import VideoUsecase


class IniciarProcessamentoService:
    def __init__(self):
        self.bucket_usecase = BucketUsecase()
        self.video_usecase = VideoUsecase()
        self.sqs_usecase = SqsUsecase()

    def iniciar_processamento(self, nome_arquivo):
        response = self.bucket_usecase.buscar_metadados_video(nome_arquivo)
        print(response)
        self.video_usecase.gravar_metadados_video(nome_arquivo)
        self.sqs_usecase.send("message")
