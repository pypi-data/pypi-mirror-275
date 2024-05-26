from django.conf import settings
from django.db.models import Model
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response

from core.base.list_schema import ListCustomSchema
from core.base.version import VersioningMixin
from core.logger import app_logger


class RetrieveMixin(RetrieveModelMixin, GenericAPIView):
    versioning_class = VersioningMixin
    swagger_schema = ListCustomSchema

    def retrieve(self, request, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger)
        logger.info(f'Retrieve request received for {self.__class__.__name__} view using version {request.version}', params=request.query_params,
                    kwargs=kwargs, args=args)
        obj: Model = self.get_object()
        logger.info(f'Retrieving {obj} with API version {request.version}')
        if request.version == settings.DEFAULT_API_VERSION:
            logger.debug(f'using default retrieve method for view: {self.__class__.__name__}')
            return super().retrieve(request, *args, **kwargs)
        else:
            logger.debug(f'using custom retrieve method for view: {self.__class__.__name__} for version {request.version}')
            retrieve_method = getattr(self, f'retrieve_v{request.version}', None)
            if retrieve_method:
                logger.debug(f'custom retrieve method found for version {request.version}')
                return retrieve_method(request, *args, **kwargs)
            else:
                logger.error(f'No custom retrieve method found for version {request.version}')
                return Response({'message': 'Implementation for this API Version not found'}, status=400)
