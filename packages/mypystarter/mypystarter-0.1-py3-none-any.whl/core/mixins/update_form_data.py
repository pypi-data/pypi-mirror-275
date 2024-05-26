from django.http import QueryDict
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from core.logger import app_logger
from core.types import IRequest


class UpdateFormDataMixin(GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = Serializer
    update_fields = []

    def partial_update(self, request: IRequest, *args, **kwargs):
        logger = getattr(request, 'logger', app_logger).bind(
            view=self.__class__.__name__, version=request.version, params=request.query_params,
            args=args, kwargs=kwargs)
        instance = self.get_object()
        logger.debug(f'partial update request received for object: {instance}')
        # noinspection PyUnresolvedReferences
        get_serializer = self.get_serializer
        serializer: Serializer = get_serializer(data=request.data)
        logger.debug(f'Validating serializer {serializer.__class__.__name__} with data {request.data}')
        update_data: QueryDict = request.data.copy()
        if self.update_fields:
            for field in update_data:
                if field not in self.update_fields:
                    del update_data[field]
        logger.debug(f'Update fields for object {instance} are {self.update_fields}')
        many_to_many_fields = getattr(serializer, 'many_to_many_fields', [])
        logger.debug(f'Many to many fields for object {instance} are {many_to_many_fields}')
        for field in many_to_many_fields:
            if field.name in update_data:
                data = update_data.getlist(field.name, '')
                if data:
                    ids = list(map(int, data.split(',')))
                    if ids:
                        update_data[field.name] = ids[0]
        serializer.is_valid(raise_exception=True)
        logger.debug(f'Serializer {serializer.__class__.__name__} is valid, proceeding with update')
        instance = serializer.update(instance, serializer.validated_data)
        response = serializer.to_representation(instance)
        logger.info(f'Object {instance} updated successfully')
        # noinspection PyUnresolvedReferences
        return Response(response, status=status.HTTP_200_OK, headers=self.get_success_headers(serializer.data))
