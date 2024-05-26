from django.contrib.auth.models import AbstractUser
from django.db.models import SmallIntegerField, CharField

USER_ROLES = (
    (1, 'Administrator'),
    (2, 'Manager'),
    (3, 'User')
)


class AppUser(AbstractUser):
    role = SmallIntegerField(choices=USER_ROLES, default=USER_ROLES[0][0])
    avatar = CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f'User #{self.pk}: {self.username} - Role: {self.role}'
