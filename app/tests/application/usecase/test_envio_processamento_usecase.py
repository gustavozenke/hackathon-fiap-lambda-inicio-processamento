import sys
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from application.usecase.envio_processamento_usecase import EnvioProcessamentoUseCase
from domain.entitites.video import Video
from domain.interfaces.sqs_repository import SqsRepository


class TestEnvioProcessamentoUseCase(unittest.TestCase):

    @patch.object(SqsRepository, 'send')
    def test_iniciar_processamento(self, mock_send):
        # Arrange
        os.environ["QUEUE_PROCESSAMENTO_URL"] = "https://queue-url-teste-unitario"

        video = Video(nome_video="video_teste.mp4",
                      nome_usuario="usuario_teste",
                      formato="mp4",
                      tamanho=500,
                      data_hora_inclusao=str(datetime.now()))

        mock_send.return_value = "Mensagem Enviada com Sucesso"

        sqs_repository_mock = MagicMock(SqsRepository)
        use_case = EnvioProcessamentoUseCase(sqs_repository=sqs_repository_mock)

        # Act
        use_case.iniciar_processamento(video)

        # Assert
        sqs_repository_mock.send.assert_called_once_with(
            {"nome_video": video.nome_video, "nome_usuario": video.nome_usuario},
            use_case.queue_processamento_url
        )
