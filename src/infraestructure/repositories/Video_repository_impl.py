import boto3

from domain.interfaces.video_repository import VideoRepository


class VideoRepositoryImpl(VideoRepository):

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('videos')

    def put_item(self, item: dict):
        return self.table.put_item(Item=item)
