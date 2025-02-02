import boto3

from domain.entitites.video import Video
from domain.interfaces.VideoRepository import VideoRepository


class VideoRepositoryImpl(VideoRepository):

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('videos')

    def gravar_metadados_video(self, video: Video) -> None:
        self.table.put_item(
            Item={
                'nome_usuario': video.nome_usuario,
                'nome_video': video.nome_video,
                'tamanho': video.tamanho,
                'formato': video.formato,
                'data_hora_inclusao': video.data_hora_inclusao
            }
        )
