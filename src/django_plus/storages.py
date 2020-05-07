from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    # location = 'static'
    pass


class MediaStorage(S3Boto3Storage):
    location = "media"


class CompressStorage(S3Boto3Storage):
    location = "CACHE"
