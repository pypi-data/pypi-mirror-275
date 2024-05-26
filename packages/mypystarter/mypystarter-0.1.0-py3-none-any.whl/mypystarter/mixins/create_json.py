from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class CreateJsonMixin(CreateModelMixin):
    """
    Create a model instance.
    """

    parser_classes = [JSONParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
