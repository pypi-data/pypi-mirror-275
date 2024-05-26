from django.db.models import CharField
from django.db.models import ForeignKey, CASCADE

from mypystarter.models import TimeStampModel, SoftDeletionModelMixin


class Folder(SoftDeletionModelMixin, TimeStampModel):
    parent = ForeignKey('mypystarter.Folder', on_delete=CASCADE, null=True, blank=True, related_name='children')
    name = CharField(max_length=255, null=True, blank=True)
    description = CharField(max_length=255, null=True, blank=True)
    is_active = CharField(max_length=255, null=True, blank=True)
    is_public = CharField(max_length=255, null=True, blank=True)
    path = CharField(max_length=255, null=True, blank=True)
