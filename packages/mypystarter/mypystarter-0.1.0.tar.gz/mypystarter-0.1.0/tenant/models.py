# Create your models here.
from datetime import datetime

from django.db import models
from django.db.models import ForeignKey

from mypystarter.models import TimeStampModel, SoftDeletionModelMixin
from mypystarter.models.archive import ArchiveModelMixin
from mypystarter.models.foreign_key_field import FileForeignKey


def upload_to(instance, filename, field_name):
    if not instance:
        return f'uploads/products/{datetime.now().timestamp()}-{filename}'
    if not hasattr(instance, 'client'):
        return f'uploads/products/{datetime.now().timestamp()}-{filename}'
    tenant_name = 'instance.client.schema_name'  # Assuming you have a 'tenant' attribute in the 'Client' model
    return f'uploads/tenants/{tenant_name}/products/{instance.pk}/{field_name}/{datetime.now().timestamp()}-{filename}'


class Product(SoftDeletionModelMixin, TimeStampModel, ArchiveModelMixin):
    name = models.CharField(max_length=100, blank=True, null=True)
    client = ForeignKey('mypystarter.Client', on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    img = FileForeignKey('mypystarter.PrivateFile', upload_to=upload_to, field_name='img', null=True, blank=True)
    img2 = FileForeignKey('mypystarter.PublicFile', upload_to='test2/', field_name='img2', many=True, null=True, blank=True)
