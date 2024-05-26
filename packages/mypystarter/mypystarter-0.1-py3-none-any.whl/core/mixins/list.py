from django.conf import settings
from rest_framework import filters
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from core.base.list_schema import ListCustomSchema
from core.base.pagination import StandardResultsSetPagination
from core.base.search_filter import MyFilterBackend
from core.base.version import VersioningMixin
from core.logger import app_logger
from core.types import IRequest


class ListMixin(ListModelMixin, GenericAPIView):
    versioning_class = VersioningMixin
    swagger_schema = ListCustomSchema
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, MyFilterBackend, OrderingFilter]
    ordering_fields = ['id']

    def list(self, request: IRequest, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger)
        logger.info(f'list request received for {self.__class__.__name__} view using version {request.version}', params=request.query_params)
        if request.version == settings.DEFAULT_API_VERSION:
            logger.debug(f'using default list method for view: {self.__class__.__name__}', default_version=settings.DEFAULT_API_VERSION)
            return super().list(request, *args, **kwargs)
        else:
            logger.debug(f'using custom list method for view: {self.__class__.__name__} for version {request.version}')
            list_method = getattr(self, f'list_v{request.version}', None)
            if list_method:
                logger.debug(f'custom list method found for version {request.version}')
                return list_method(request, *args, **kwargs)
            else:
                logger.error(f'No custom list method found for version {request.version}')
                return Response({'message': 'Implementation for this API Version not found'}, status=400)

    def get_paginated_response(self, data):
        if not self.request.query_params.get('page'):
            return Response(data)
        return super().get_paginated_response(data)
