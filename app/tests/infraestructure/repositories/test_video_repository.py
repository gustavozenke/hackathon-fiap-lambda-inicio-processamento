import os
import sys
import unittest
from unittest.mock import patch, MagicMock

import boto3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from infraestructure.repositories.video_repository_impl import VideoRepositoryImpl


class TestVideoRepositoryImpl(unittest.TestCase):

    @patch.object(boto3, 'resource')
    def test_put_item(self, mock_boto_resource):
        # Arrange
        mock_dynamodb_resource = MagicMock()
        mock_table = MagicMock()
        mock_boto_resource.return_value = mock_dynamodb_resource
        mock_dynamodb_resource.Table.return_value = mock_table

        video_repository = VideoRepositoryImpl()

        item = {
            'nome_video': 'video_teste.mp4',
            'nome_usuario': 'usuario_teste',
            'tamanho': 500,
            'formato': 'mp4',
            'data_hora_inclusao': '2025-02-09T10:00:00'
        }

        # Act
        video_repository.put_item(item)

        # Assert
        mock_table.put_item.assert_called_once_with(Item=item)
