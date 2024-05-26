from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc: Exception, context) -> Response:
    response = exception_handler(exc, context)
    print('dd')
    if isinstance(exc, Http404):
        print('404')
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"error": 'error'})
