from django.db.models import FileField

from core.storages.s3 import PublicS3Storage


class S3FileField(FileField):
    def __init__(self, *args, **kwargs):
        self.storage = PublicS3Storage()
        self.is_public = kwargs.pop('is_public', True)
        super().__init__(*args, **kwargs)
