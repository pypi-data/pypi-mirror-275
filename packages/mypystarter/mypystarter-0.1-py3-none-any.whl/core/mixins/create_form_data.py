from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class CreateFormDataMixin(CreateModelMixin):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class: Serializer = None
    action: str = None

    def create(self, request, *args, **kwargs):
        # noinspection PyUnresolvedReferences
        get_serializer = self.get_serializer
        serializer = get_serializer(data=request.data)
        many_to_many_fields = getattr(serializer, 'many_to_many_fields', [])
        for field in many_to_many_fields:
            if field.name in request.data:
                data = request.data.getlist(field.name, '')
                if data:
                    ids = list(map(int, data.split(',')))
                    if ids:
                        request.data[field.name] = ids[0]
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.action = 'retrieve'
        # noinspection PyUnresolvedReferences
        retrieve_serializer = self.get_serializer(instance, context={'request': request})
        response = retrieve_serializer.to_representation(instance)
        return Response(response, status=status.HTTP_201_CREATED, headers=self.get_success_headers(retrieve_serializer.data))
