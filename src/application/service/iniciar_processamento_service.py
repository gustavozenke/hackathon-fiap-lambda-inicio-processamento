from application.usecase.sqs_usecase import SqsUsecase
from application.usecase.video_usecase import VideoUsecase


class IniciarProcessamentoService:
    def __init__(self):
        self.video_usecase = VideoUsecase()
        self.sqs_usecase = SqsUsecase()
        self.queue_processamento_url = "https://sqs.us-east-1.amazonaws.com/369780787289/sqs-processamento"

    def iniciar_processamento(self, nome_video, tamanho):
        nome_usuario = nome_video.split('-')[0]
        formato = nome_video.split('.')[1]

        self.video_usecase.gravar_metadados_video(nome_video, nome_usuario, formato, tamanho)

        self.sqs_usecase.send(self.formatar_mensagem_queue_processamento(nome_video, nome_usuario),
                              self.queue_processamento_url)

    @staticmethod
    def formatar_mensagem_queue_processamento(nome_video, nome_usuario):
        return {
            "nome_video": nome_video,
            "nome_usuario": nome_usuario
        }
