from drf_yasg import openapi
from rest_framework import serializers


class UploadSerializer(serializers.Serializer):
    file = serializers.FileField(required=False)
    files = serializers.FileField(required=False)
    description = serializers.CharField(max_length=255, required=False)
    title = serializers.CharField(max_length=255, required=False)

    @staticmethod
    def get_file_param():
        return [
            openapi.Parameter(
                name='fields',
                in_=openapi.IN_QUERY,
                description='selected fields',
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING)
            ),
            openapi.Parameter(
                name='populate',
                in_=openapi.IN_QUERY,
                description='selected fields',
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING)
            ),
            openapi.Parameter(
                name='exclude',
                in_=openapi.IN_QUERY,
                description='selected fields',
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING)
            ),
        ]
