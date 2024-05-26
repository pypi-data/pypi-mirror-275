import uuid

from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE
from django_tenants.models import TenantMixin, DomainMixin

from core.models import SoftDeletionModelMixin, TimeStampModel


class Country(Model):
    name = CharField(max_length=200, null=True, blank=True)
    nativeName = CharField(max_length=200, null=True, blank=True, default=f'Country {uuid.uuid4()}')
    isoCode = CharField(max_length=200, null=True, blank=True, default='123')


# Create your models here.

class City(Model):
    name = CharField(max_length=200, null=True, blank=True)
    nativeName = CharField(max_length=200, null=True, blank=True, default=f'City {uuid.uuid4()}')
    zip = CharField(max_length=200, null=True, blank=True, default='123')
    country = ForeignKey('core.Country', on_delete=CASCADE, null=True, blank=True, related_name='cities')


class Client(TenantMixin, SoftDeletionModelMixin, TimeStampModel):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    city = ForeignKey('core.City', on_delete=CASCADE, null=True, blank=True)
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass
