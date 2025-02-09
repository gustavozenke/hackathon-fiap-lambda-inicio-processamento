import json
import os
import sys
import unittest
from unittest.mock import patch, Mock

import boto3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from infraestructure.repositories.sqs_repositrory import SqsRepositoryImpl
from infraestructure.repositories.video_repository_impl import VideoRepositoryImpl
from application.service.iniciar_processamento_service import IniciarProcessamentoService
from application.entrypoint.lambda_handler import lambda_handler


class TestLambdaHandler(unittest.TestCase):

    @patch.object(boto3, 'resource')
    @patch.object(boto3, 'client')
    @patch.object(SqsRepositoryImpl, 'send')
    @patch.object(VideoRepositoryImpl, 'put_item')
    @patch.object(IniciarProcessamentoService, 'execute')
    def test_lambda_handler(self, mock_execute, mock_sqs, mock_repository, mock_boto_client, mock_boto_resource):
        # Arrange
        mock_sqs.return_value = None
        mock_repository.return_value = None
        mock_execute.return_value = None
        mock_boto_client.return_value = None
        mock_boto_resource.return_value = Mock()

        event = {"Records": [
            {"body": json.dumps({"Records": [{"s3": {"object": {"key": "video_teste.mp4", "size": 500}}}]})}]
        }

        # Act
        response = lambda_handler(event, {})

        # Arrange
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], 'Mensagem processada com sucesso!')

        mock_execute.assert_called_once_with("video_teste.mp4", 500)
