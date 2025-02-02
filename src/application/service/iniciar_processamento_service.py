from application.usecase.sqs_usecase import SqsUsecase
from application.usecase.video_usecase import VideoUsecase
from domain.enums.status_processamento import StatusProcessamento


class IniciarProcessamentoService:
    def __init__(self):
        self.video_usecase = VideoUsecase()
        self.sqs_usecase = SqsUsecase()
        self.queue_status_url = "https://sqs.us-east-1.amazonaws.com/369780787289/sqs-gravar-status-processamento"
        self.queue_processamento_url = "https://sqs.us-east-1.amazonaws.com/369780787289/sqs-processamento"

    def iniciar_processamento(self, nome_arquivo, tamanho):
        nome_usuario = nome_arquivo.split('-')[0]
        formato = nome_arquivo.split('.')[1]

        self.video_usecase.gravar_metadados_video(nome_arquivo, nome_usuario, formato, tamanho)

        self.sqs_usecase.send(self.formatar_mensagem_queue_status(nome_arquivo, nome_usuario),
                              self.queue_status_url)

        self.sqs_usecase.send(self.formatar_mensagem_queue_processamento(nome_arquivo, nome_usuario),
                              self.queue_processamento_url)

    @staticmethod
    def formatar_mensagem_queue_processamento(nome_arquivo, nome_usuario):
        return {
            "nome_arquivo": nome_arquivo,
            "nome_usuario": nome_usuario
        }

    def formatar_mensagem_queue_status(self, nome_arquivo, nome_usuario):
        message = self.formatar_mensagem_queue_processamento(nome_arquivo, nome_usuario)
        message['status_processamento'] = StatusProcessamento.PROCESSAMENTO_INICIADO.name
        return message
