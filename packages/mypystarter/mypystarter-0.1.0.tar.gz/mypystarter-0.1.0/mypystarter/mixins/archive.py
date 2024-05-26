from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.utils import timezone
from drf_yasg.openapi import IN_QUERY, Parameter, TYPE_ARRAY, Items, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from mypystarter.logger import app_logger
from mypystarter.mixins.list import ListMixin


class ArchiveMixin(ListMixin):
    archive_relations_to_check = []

    def list(self, request, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(
            params=request.query_params, args=args, kwargs=kwargs, view=self.__class__.__name__,
            version=request.version)
        logger.info(f'archive list request received')
        queryset = self.get_queryset() or self.queryset
        logger.debug(f'filtering out archived objects')
        queryset = self.filter_queryset(queryset).filter(archived_at__isnull=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            logger.debug('Pagination requested, returning paginated response')
            serializer = self.get_serializer(page, many=True)
            logger.info('archive list request completed successfully', serializer=serializer.__class__)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True) or self.serializer_class or Serializer
        logger.debug('No pagination requested, returning full response', serializer=serializer.__class__)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(
            params=request.query_params, args=args, kwargs=kwargs, view=self.__class__.__name__,
            version=request.version)
        logger.info('archive retrieve request received')
        instance = self.get_object()
        logger.debug(f'checking if object {instance} is archived')
        if instance.archived_at is not None:
            logger.warning(f'Object {instance} is archived, returning 404')
            raise Http404
        serializer = self.get_serializer(instance)
        logger.debug(f'Object {instance} is not archived, returning object', serializer=serializer.__class__)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def archived(self, request):
        logger = getattr(request, 'logger', app_logger).bind(params=request.query_params, view=self.__class__.__name__, version=request.version)
        logger.info('archived list request received')
        queryset = self.get_queryset() or self.queryset
        logger.debug('filtering out non-archived objects')
        queryset = self.filter_queryset(queryset).filter(archived_at__isnull=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            logger.debug('Pagination requested, returning paginated response')
            serializer = self.get_serializer(page, many=True)
            logger.info('archived list request completed successfully', serializer=serializer.__class__)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        logger.debug('No pagination requested, returning full response', serializer=serializer.__class__)
        return Response(serializer.data)

    # retrieve deleted object
    @action(detail=False, methods=['GET'], url_path="archived/(?P<pk>[^/.]+)")
    def retrieve_archived(self, request, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(params=request.query_params, args=args, kwargs=kwargs, view=self.__class__.__name__,
                                                             version=request.version)
        logger.info('archived retrieve request received')
        queryset = self.get_queryset() or self.queryset
        instance = queryset.filter(pk=kwargs['pk']).first()
        logger.debug(f'checking if object {instance} exists')
        if not instance:
            logger.warning(f'Object with pk {kwargs["pk"]} not found, returning 404')
            raise Http404
        logger.debug(f'Object {instance} exists, returning object')
        serializer = self.get_serializer(instance) or self.serializer_class or Serializer
        logger.info('archived retrieve request completed successfully', serializer=serializer.__class__)
        return Response(serializer.data)

    @swagger_auto_schema(method='patch', manual_parameters=[Parameter('ids', IN_QUERY, type=TYPE_ARRAY, items=Items(type=TYPE_INTEGER))])
    @action(detail=False, methods=['PATCH'], url_path="archive", serializer_class=Serializer)
    def group_archive(self, request: Request):
        logger = getattr(request, 'logger', app_logger).bind(params=request.query_params, view=self.__class__.__name__, version=request.version)
        logger.info('archive group request received')
        ids = request.query_params.getlist('ids', [])
        if len(ids) == 1:
            ids = ids[0].split(',')
        logger.debug(f'Archiving {len(ids)} records with ids {ids}')
        user = getattr(request, 'user', None)
        if not user or isinstance(user, AnonymousUser):
            logger.warning('User is Anonymous, setting user to None')
            user = None
        queryset = self.get_queryset() or self.queryset
        logger.debug('Proceeding to archive records')
        num = queryset.filter(pk__in=ids).update(archived_by=user, archived_at=timezone.now())
        logger.info(f'{num} records archived successfully')
        return Response({'message': f"{num} records Archived Successfully"})

    @swagger_auto_schema(method='patch', manual_parameters=[Parameter('ids', IN_QUERY, type=TYPE_ARRAY, items=Items(type=TYPE_INTEGER))])
    @action(detail=False, methods=['patch'], url_path="archived/unarchive", serializer_class=Serializer)
    def group_unarchive(self, request: Request):
        logger = getattr(request, 'logger', app_logger).bind(params=request.query_params, view=self.__class__.__name__, version=request.version)
        logger.info('unarchive group request received')
        ids = request.query_params.getlist('ids', [])
        if len(ids) == 1:
            ids = ids[0].split(',')
        logger.debug(f'Un-archiving {len(ids)} records with ids {ids}')
        queryset = self.get_queryset() or self.queryset
        num = queryset.filter(pk__in=ids).update(archived_by=None, archived_at=None)
        if num:
            logger.info(f'{num} records unarchived successfully')
            return Response({'message': f"Unarchived {num} records successfully"})
        else:
            logger.info('No records to unarchive')
            return Response({'message': "No records to restore"})
