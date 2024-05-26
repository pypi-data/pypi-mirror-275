from django_filters.rest_framework import DjangoFilterBackend

from mypystarter.logger import app_logger


class MyFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        logger = getattr(request, 'logger', app_logger)
        params = request.query_params
        kwargs = dict()
        if hasattr(view, 'filterset'):
            for k, v in params.items():
                if k in view.filterset:
                    kwargs[k] = v
        if kwargs:
            logger.info(f'Queryset filtered using params: {kwargs}')
        return queryset.filter(**kwargs)
