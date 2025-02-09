import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from application.usecase.gravar_video_usecase import GravarVideoUseCase
from domain.entitites.video import Video
from domain.interfaces.video_repository import VideoRepository


class TestGravarVideoUseCase(unittest.TestCase):

    @patch.object(VideoRepository, 'put_item')
    def test_gravar_metadados_video(self, mock_put_item):
        video = Video(
            nome_video="video_teste.mp4",
            nome_usuario="usuario_teste",
            tamanho=500,
            formato="mp4",
            data_hora_inclusao="2025-02-09T10:00:00"
        )

        mock_put_item.return_value = "Item Persistido com Sucesso"

        video_repository_mock = MagicMock(VideoRepository)
        use_case = GravarVideoUseCase(video_repository=video_repository_mock)

        use_case.gravar_metadados_video(video)

        video_repository_mock.put_item.assert_called_once_with({
            'nome_usuario': video.nome_usuario,
            'nome_video': video.nome_video,
            'tamanho': video.tamanho,
            'formato': video.formato,
            'data_hora_inclusao': video.data_hora_inclusao
        })
