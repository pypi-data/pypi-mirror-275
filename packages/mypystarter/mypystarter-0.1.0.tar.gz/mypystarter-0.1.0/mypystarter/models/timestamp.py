from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        'mypystarter.AppUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_%(class)ss'
    )
    updated_by = models.ForeignKey(
        'mypystarter.AppUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_%(class)ss'
    )

    class Meta:
        abstract = True
