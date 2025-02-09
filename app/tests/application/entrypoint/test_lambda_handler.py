import json
import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from application.service.iniciar_processamento_service import IniciarProcessamentoService
from application.entrypoint.lambda_handler import lambda_handler


class TestLambdaHandler(unittest.TestCase):

    @patch.object(IniciarProcessamentoService, 'execute')
    def test_lambda_handler(self, mock_execute):
        # Arrange
        mock_execute.return_value = None

        event = {"Records": [
            {"body": json.dumps({"Records": [{"s3": {"object": {"key": "video_teste.mp4", "size": 500}}}]})}]
        }

        # Act
        response = lambda_handler(event, {})

        # Arrange
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], 'Mensagem processada com sucesso!')

        mock_execute.assert_called_once_with("video_teste.mp4", 500)
