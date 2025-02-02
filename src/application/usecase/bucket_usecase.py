import boto3


class BucketUsecase:

    def __init__(self):
        self.s3_client = boto3.client('s3')

    def buscar_metadados_video(self, nome_arquivo):
        response = self.s3_client.head_object(Bucket="bucket-hackathon-fiap-raw-videos", Key=nome_arquivo)
        return response['Metadata']
