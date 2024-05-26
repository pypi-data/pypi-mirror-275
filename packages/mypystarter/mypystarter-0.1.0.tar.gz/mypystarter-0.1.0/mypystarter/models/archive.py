from django.db import models
from django.utils import timezone


class ArchiveModelMixin(models.Model):
    archived_at = models.DateTimeField(default=None, null=True, blank=True)
    archived_by = models.ForeignKey(
        'mypystarter.AppUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='archived_%(class)ss'
    )

    class Meta:
        abstract = True
        ordering = ['id']

    def archive(self, *args, **kwargs):
        user = kwargs.get('user', None)
        if user and hasattr(user, 'id'):
            self.archived_by = user
        self.archived_at = timezone.now()
        self.save()

    def unarchive(self, *args, **kwargs):
        self.archived_by = None
        self.archived_at = None
        self.save()
