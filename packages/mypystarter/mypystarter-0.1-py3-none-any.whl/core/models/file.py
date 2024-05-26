# class for uploaded file as django db model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import FileField

from core.models.soft import SoftDeletionModelMixin
from core.models.timestamp import TimeStampModel
from core.storages.s3 import S3PrivateStorage, S3PublicStorage


class File(SoftDeletionModelMixin, TimeStampModel):
    mime_type = models.CharField(max_length=255, null=True, blank=True)
    size = models.BigIntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    filename = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=False)
    folder = models.ForeignKey('core.Folder', on_delete=models.CASCADE, null=True, blank=True)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __init__(self, *args, **kwargs):
        self.many = kwargs.pop('many', False) if 'many' in kwargs else False
        self.upload_to = kwargs.pop('upload_to') if 'upload_to' in kwargs else None
        self.field_name = kwargs.pop('field_name') if 'field_name' in kwargs else None
        self.remote_field = kwargs.get('content_object')
        super().__init__(*args, **kwargs)  # Call the parent class constructor

    def save(self, *args, **kwargs):
        if self.upload_to:
            if isinstance(self.upload_to, str):
                # noinspection PyUnresolvedReferences
                self.file.upload_to = self.upload_to
            elif callable(self.upload_to):
                # noinspection PyUnresolvedReferences
                self.file.name = self.upload_to(self.remote_field, self.file.name, self.field_name)
            else:
                raise ValueError('upload_to must be a string or a callable')
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class PublicFile(File):
    file = FileField(storage=S3PublicStorage(), upload_to='uploads/')

    class Meta:
        db_table = 'public_files'


class PrivateFile(File):
    file = FileField(storage=S3PrivateStorage())

    class Meta:
        db_table = 'private_files'
