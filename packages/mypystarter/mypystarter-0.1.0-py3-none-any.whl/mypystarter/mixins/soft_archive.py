from django.http import Http404
from rest_framework.response import Response

from mypystarter.logger import app_logger
from mypystarter.mixins.archive import ArchiveMixin
from mypystarter.mixins.soft import SoftDeleteMixin


class SoftArchiveMixin(SoftDeleteMixin, ArchiveMixin):

    def get_queryset(self):
        logger = getattr(self.request, 'logger', app_logger).bind(view=self.__class__.__name__, version=self.request.version)
        logger.debug(f'get_queryset called for soft archive')
        queryset = super().get_queryset()
        return queryset.filter(deleted_at__isnull=True)

    def list(self, request, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version, params=request.query_params,
                                                             args=args, kwargs=kwargs)
        logger.info('soft archive list request received, filtering out deleted objects')
        queryset = self.filter_queryset(self.get_queryset()).filter(archived_at__isnull=True, deleted_at__isnull=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            logger.debug('Pagination requested, returning paginated response')
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        logger.debug('No pagination requested, returning full response')
        serializer = self.get_serializer(queryset, many=True)
        logger.info('soft archive list request completed successfully', serializer=serializer.__class__)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(
            view=self.__class__.__name__, version=request.version, params=request.query_params,
            args=args, kwargs=kwargs)
        logger.info('soft archive retrieve request received')
        instance = self.get_object()
        logger.debug(f'checking if object {instance} is deleted or archived')
        if instance.archived_at is not None:
            logger.warning(f'Object {instance} is archived, returning 404')
            raise Http404
        if instance.deleted_at is not None:
            logger.warning(f'Object {instance} is deleted, returning 404')
            raise Http404
        serializer = self.get_serializer(instance)
        logger.debug(f'Object {instance} is not deleted or archived, returning object', serializer=serializer.__class__)
        logger.info('soft archive retrieve request completed successfully')
        return Response(serializer.data)
