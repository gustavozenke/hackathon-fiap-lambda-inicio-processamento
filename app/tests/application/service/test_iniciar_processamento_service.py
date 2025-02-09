import os
import sys
import unittest
from unittest.mock import patch, MagicMock, ANY

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from domain.interfaces.envio_processamento import EnvioProcessamento
from domain.interfaces.gravar_video import GravarVideo
from application.service.iniciar_processamento_service import IniciarProcessamentoService


class TestIniciarProcessamentoService(unittest.TestCase):

    @patch.object(GravarVideo, 'gravar_metadados_video')
    @patch.object(EnvioProcessamento, 'iniciar_processamento')
    def test_execute_sucesso(self, mock_iniciar_processamento, mock_gravar_metadados_video):
        # Arrange
        gravar_video_usecase = MagicMock(GravarVideo)
        enviar_processamento_usecase = MagicMock(EnvioProcessamento)

        gravar_video_usecase.gravar_metadados_video = mock_gravar_metadados_video
        enviar_processamento_usecase.iniciar_processamento = mock_iniciar_processamento

        service = IniciarProcessamentoService(gravar_video_usecase, enviar_processamento_usecase)

        nome_video = "usuario-video.mp4"
        tamanho = 5000

        # Act
        service.execute(nome_video, tamanho)

        # Assert
        mock_gravar_metadados_video.assert_called_once_with(ANY)
        mock_iniciar_processamento.assert_called_once_with(ANY)

    @patch.object(EnvioProcessamento, 'iniciar_processamento')
    def test_execute_exception(self, mock_iniciar_processamento):
        # Arrange
        gravar_video_usecase = MagicMock(GravarVideo)
        gravar_video_usecase.gravar_metadados_video.side_effect = Exception("Erro ao gravar metadados")
        enviar_processamento_usecase = MagicMock(EnvioProcessamento)
        service = IniciarProcessamentoService(gravar_video_usecase, enviar_processamento_usecase)

        nome_video = "usuario-video.mp4"
        tamanho = 5000

        # Act & Assert
        with self.assertRaises(Exception) as context:
            service.execute(nome_video, tamanho)

        self.assertEqual(str(context.exception), "Erro ao gravar metadados")
        mock_iniciar_processamento.assert_not_called()
