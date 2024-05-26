from django.conf import settings
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from core.logger import app_logger
from core.types import IRequest


class GenericView(GenericViewSet):
    ordering_fields = '__all__'
    search_fields = []  # list of fields that can be used to search the queryset
    queryset = None
    serializer_class = None
    serializer_action_classes_per_version = {}  # dict of version to dict of action to serializer
    filter_backends = []  # list of filter backends to apply to the view
    filterset = []  # list of fields that can be used to filter the queryset
    request: IRequest = None

    def get_serializer_class(self, custom_action=None):
        default_version = settings.DEFAULT_API_VERSION
        request = self.request
        logger = getattr(request, 'logger', app_logger).bind(serializers=self.serializer_action_classes_per_version, default_version=default_version)
        logger.debug(f'get_serializer_class called for view: {self.__class__.__name__}, action: {self.action}, version: {request.version}')
        # Get the corresponding serializer or return the default serializer.
        current_version_serializers = self.serializer_action_classes_per_version.get(settings.DEFAULT_API_VERSION, {})
        action = custom_action or self.action
        serializer = current_version_serializers.get(action, None)
        if serializer:
            logger.debug(f'serializer found for action: {action}', serializer=serializer)
            return serializer
        else:
            if self.serializer_class:
                logger.debug(f'No custom serializer for action {action}. Using {self.serializer_class} for view: {self.__class__.__name__}')
                return self.serializer_class
            else:
                logger.error(f'no serializer found for action: {action}, using default DRF serializer <Serializer>')
                return Serializer

    def filter_queryset(self, queryset):
        logger = getattr(self.request, 'logger', app_logger)
        # Apply filters to queryset using filter_backends classes in the order they are defined.
        if self.filter_backends:
            logger.debug('Applying filters on the queryset', filters=self.filter_backends)
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        logger = getattr(self.request, 'logger', app_logger)
        # Get the queryset for this view. This must be an iterable, and may be a queryset.
        queryset = super().get_queryset()
        # use the queryset defined in the view if it exists
        logger.debug(f'get_queryset called for view: {self.__class__.__name__} using version {self.request.version}',
                     queryset_is_null=queryset is None, self_queryset_is_null=self.queryset is None)
        return self.queryset if queryset is None else queryset
