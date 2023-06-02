import boto3
from decouple import config
from django.apps import AppConfig


class AppMicrosoftConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_microsoft"

    def ready(self):
        s3 = boto3.client(
            "s3",
            aws_access_key_id=config("S3KEY"),
            aws_secret_access_key=config("S3SECRET"),
        )
        s3.download_file("trsu-secrets", config("KEY"), f"./{config('KEY')}")
