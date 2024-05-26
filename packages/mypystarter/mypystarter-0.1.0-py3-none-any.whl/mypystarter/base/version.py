from django.conf import settings
from rest_framework.versioning import QueryParameterVersioning


class VersioningMixin(QueryParameterVersioning):
    version_param = 'v'
    default_version = settings.DEFAULT_API_VERSION
    allowed_versions = settings.ALLOWED_API_VERSIONS
