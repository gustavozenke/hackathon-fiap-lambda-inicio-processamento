import json
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

import boto3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from infraestructure.repositories.sqs_repositrory import SqsRepositoryImpl


class TestSqsRepository(unittest.TestCase):

    @patch.object(boto3, 'client')
    def test_send_message(self, mock_boto_client):
        # Arrange
        mock_sqs_client = MagicMock()
        mock_boto_client.return_value = mock_sqs_client

        sqs_repository = SqsRepositoryImpl()

        message = {"nome_video": "video_teste.mp4", "nome_usuario": "usuario_teste"}
        queue_url = "https://sqs.us-east-1.amazonaws.com/123456789012/queue_testee_unitario"

        # Act
        sqs_repository.send(message, queue_url)

        # Assert
        mock_sqs_client.send_message.assert_called_once_with(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )
