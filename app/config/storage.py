from storages.backends.s3boto3 import S3Boto3Storage


class StaticFilesStorage(S3Boto3Storage):
    location = 'static'


class DefaultFilesStorage(S3Boto3Storage):
    location = 'media'
