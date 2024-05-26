from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from drf_yasg.openapi import IN_QUERY, Parameter, TYPE_ARRAY, Items, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from mypystarter.logger import app_logger
from mypystarter.mixins.list import ListMixin
from mypystarter.models import SoftDeletionModelMixin
from mypystarter.types import IRequest


class SoftDeleteMixin(ListMixin):
    deleted_relations_to_check = []
    all_queryset = None

    def list(self, request: IRequest, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger)
        logger.info(f'soft list request received for {self.__class__.__name__} view using version {request.version}',
                    params=request.query_params, args=args, kwargs=kwargs)
        queryset = self.filter_queryset(self.get_queryset()).filter(deleted_at__isnull=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            logger.debug('Pagination requested, returning paginated response', serializer=serializer.__class__)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        logger.debug(f'No pagination requested, returning full response')
        logger.info('Soft list request completed successfully', serializer=serializer.__class__)
        return Response(serializer.data)

    def retrieve(self, request: IRequest, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger)
        logger.info(f'soft retrieve request received for {self.__class__.__name__} view using version {request.version}',
                    params=request.query_params, args=args, kwargs=kwargs)
        instance = self.get_object()
        if instance.deleted_at is not None:
            logger.warning(f'Object {instance} is deleted, returning 404')
            raise Http404
        logger.debug(f'Object {instance} is not deleted, returning object')
        serializer = self.get_serializer(instance)
        logger.info('Soft retrieve request completed successfully', serializer=serializer.__class__)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def deleted(self, request: IRequest):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version)
        logger.info(f'soft deleted list request received', params=request.query_params)
        if self.all_queryset is None:
            logger.error('all_queryset is not defined')
            raise ValidationError({'error': "all_queryset is not defined"})
        logger.debug(f'all_queryset found, filtering deleted objects')
        queryset = self.filter_queryset(self.all_queryset).filter(deleted_at__isnull=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            logger.debug('Pagination requested, returning paginated response', serializer=serializer.__class__)
            return self.get_paginated_response(serializer.data)
        logger.debug('No pagination requested, returning full response')
        serializer = self.get_serializer(queryset, many=True)
        logger.info('Soft deleted list request completed successfully', serializer=serializer.__class__)
        return Response(serializer.data)

    # retrieve deleted object
    @action(detail=False, methods=['GET'], url_path="deleted/(?P<pk>[^/.]+)")
    def retrieve_deleted(self, request: IRequest, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version, args=args, kwargs=kwargs)
        logger.info(f'soft retrieve deleted request received', params=request.query_params)
        if self.all_queryset is None:
            logger.error('all_queryset is not defined')
            raise ValidationError({'error': "all_queryset is not defined"})
        logger.debug(f'all_queryset found, filtering deleted objects by pk')
        instance = self.all_queryset.filter(pk=kwargs.get('pk')).first()
        if not instance:
            logger.warning(f'Object with pk {kwargs.get("pk")} not found, returning 404')
            raise Http404
        logger.debug(f'Object {instance} found, returning object')
        serializer = self.get_serializer(instance) or self.serializer_class
        logger.info('Soft retrieve deleted request completed successfully', serializer=serializer.__class__)
        return Response(serializer.data)

    def destroy(self, request: IRequest, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version, args=args, kwargs=kwargs)
        logger.info(f'soft delete request received', params=request.query_params)
        obj = self.get_object()
        if isinstance(obj, SoftDeletionModelMixin):
            logger.info(f'Object {obj} is a SoftDeletionModelMixin, soft deleting')
            user = getattr(request, 'user', None)
            if not user or isinstance(user, AnonymousUser):
                logger.warning('User is AnonymousUser, setting user to None')
                user = None
            logger.debug(f'Proceeding to soft delete object {obj}')
            obj.delete(user=user)
        else:
            logger.warning(f'Object {obj} is not a SoftDeletionModelMixin, doing classic delete')
            obj.delete()
        serializer = self.get_serializer_class() or self.serializer_class
        logger.info('Soft delete request completed successfully', serializer=serializer.__class__)
        return Response(status=200, data=serializer(obj).data)

    @swagger_auto_schema(method='delete', manual_parameters=[Parameter('ids', IN_QUERY, type=TYPE_ARRAY, items=Items(type=TYPE_INTEGER))])
    @action(detail=False, methods=['DELETE'], url_path="deleted/hard_delete", serializer_class=Serializer)
    def group_destroy(self, request: IRequest):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version)
        logger.info(f'soft delete request received', params=request.query_params)
        ids = request.query_params.getlist('ids', [])
        if len(ids) == 1:
            ids = ids[0].split(',')
        logger.debug(f'Proceeding to soft delete objects with ids {ids}')
        num, _ = self.all_queryset.filter(pk__in=ids).hard_delete()
        logger.info(f'{num} records Destroyed Successfully')
        return Response({'message': f"{num} records Destroyed Successfully"})

    @swagger_auto_schema(method='post', manual_parameters=[Parameter('ids', IN_QUERY, type=TYPE_ARRAY, items=Items(type=TYPE_INTEGER))])
    @action(detail=False, methods=['POST'], url_path="deleted/restore", serializer_class=Serializer)
    def group_restore(self, request: IRequest):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version)
        logger.info(f'soft restore request received', params=request.query_params)
        ids = request.query_params.getlist('ids', [])
        if len(ids) == 1:
            ids = ids[0].split(',')
        logger.debug(f'Proceeding to restore objects with ids {ids}')
        num = self.all_queryset.filter(pk__in=ids).update(deleted_by=None, deleted_at=None)
        if num:
            logger.info(f'{num} records Restored Successfully')
            return Response({'message': f"Restored {num} records successfully"})
        else:
            logger.info('No records to restore')
            return Response({'message': "No records to restore"})

    @swagger_auto_schema(method='delete', manual_parameters=[Parameter('ids', IN_QUERY, type=TYPE_ARRAY, items=Items(type=TYPE_INTEGER))])
    @action(detail=False, methods=['DELETE'], url_path="delete", serializer_class=Serializer)
    def group_soft_delete(self, request: IRequest):
        logger = getattr(request, 'logger', app_logger).bind(view=self.__class__.__name__, version=request.version, params=request.query_params)
        logger.info(f'soft delete request received')
        ids = request.query_params.getlist('ids', [])
        if len(ids) == 1:
            ids = ids[0].split(',')
        logger.debug(f'Proceeding to soft delete objects with ids {ids}')
        user = getattr(request, 'user', None)
        if not user or isinstance(user, AnonymousUser):
            logger.warning('User is AnonymousUser, setting user to None')
            user = None
        logger.debug(f'Proceeding to soft delete objects with ids {ids}')
        num = self.all_queryset.filter(pk__in=ids).delete(user=user)
        if num:
            logger.info(f'Soft Deleted {num} records successfully')
            return Response({'message': f"Soft Deleted {num} records successfully"})
        else:
            logger.info('No records to soft delete')
            return Response({'message': "No records to soft delete"})
