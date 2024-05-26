from collections import OrderedDict
from importlib import import_module

from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer

from core.logger import app_logger


class ReadSerializer(ModelSerializer):
    global_populate_serializers = {
        'created_by': 'tenant.UserSerializer',
        'updated_by': 'tenant.UserSerializer',
        'deleted_by': 'tenant.UserSerializer',
        'restored_by': 'tenant.UserSerializer',
    }
    populate_serializers = {
        'client': 'tenant.ClientSerializer',
        'city': 'tenant.CitySerializer',
        'country': 'tenant.CountrySerializer',
    }
    selected_fields: list[str] = []
    populate_fields: list[str] = []
    excluded_fields: list[str] = []

    model_fields_names: list[str] = []
    populate_hierarchy: dict = {}
    selected_hierarchy: dict = {}
    exclude_hierarchy: dict = {}

    generic_relations_names: str = []

    def parse_request_fields(self, kwargs: dict, param='fields') -> list[str]:
        request: Request = kwargs.get('context', {}).get('request')
        if request and request.query_params.get(param):
            fs = request.query_params.getlist(param, [])
            if len(fs) == 1:
                fs = fs[0].split(',')
            return fs

    def __init__(self, *args, **kwargs_args):
        kwargs = kwargs_args.copy()
        self.selected_hierarchy = dict()
        self.selected_fields = []
        context = kwargs.get('context', {})
        request = context.get('request') if context else None
        logger = getattr(request, 'logger', app_logger) if request else context.get('logger', app_logger) or app_logger
        logger.debug(f'calling constructor of serializer {self.__class__.__name__}')
        if hasattr(self, 'Meta') and hasattr(self.Meta, 'model'):
            # noinspection PyProtectedMember
            model_fields = set(self.Meta.model._meta.get_fields())
            self.file_fields = [
                field
                for field in model_fields
                if field.related_model and field.related_model.__name__ in ['PrivateFile', 'PublicFile']
            ]
            self.relation_fields = [
                field
                for field in model_fields
                if field.is_relation and field not in self.file_fields
            ]
            self.model_fields_names = [field.name for field in model_fields]
            self.file_fields_names = [field.name for field in self.file_fields]
            self.relation_fields_names = [field.name for field in self.relation_fields]
            logger.debug(f'Got file fields and model fields and relation fields',
                         file_fields=self.file_fields_names, relation_fields=self.relation_fields_names, model_fields=self.model_fields_names)
        if 'populate_hierarchy' in kwargs_args:
            logger.debug(f'Populate hierarchy found in kwargs, updating populate hierarchy')
            self.populate_hierarchy.update(**kwargs.pop('populate_hierarchy', {}))
            self.populate_fields = self.populate_fields + list(self.populate_hierarchy.keys())
            logger.debug(f'Populate fields updated with populate hierarchy', populate_fields=self.populate_fields,
                         populate_hierarchy=self.populate_hierarchy)
        if 'selected_hierarchy' in kwargs_args:
            logger.debug(f'Selected hierarchy found in kwargs, updating selected hierarchy')
            self.selected_hierarchy.update(**kwargs.pop('selected_hierarchy', {}))
            self.selected_fields = self.selected_fields + list(self.selected_hierarchy.keys())
            logger.debug(f'Selected fields updated with selected hierarchy', selected_fields=self.selected_fields,
                         selected_hierarchy=self.selected_hierarchy)
        if 'exclude_hierarchy' in kwargs_args:
            logger.debug(f'Exclude hierarchy found in kwargs, updating exclude hierarchy')
            self.exclude_hierarchy.update(**kwargs.pop('exclude_hierarchy', {}))
            self.excluded_fields = self.excluded_fields + list(self.exclude_hierarchy.keys())
            logger.debug(f'Excluded fields updated with exclude hierarchy', excluded_fields=self.excluded_fields,
                         exclude_hierarchy=self.exclude_hierarchy)

        if 'only' in kwargs_args:
            logger.debug(f'Only fields found in kwargs, updating selected fields')
            self.selected_fields = self.selected_fields + kwargs.pop('only', [])
            logger.debug(f'Selected fields updated with only fields', selected_fields=self.selected_fields)
        if 'populate' in kwargs_args:
            logger.debug(f'Populate fields found in kwargs, updating populate fields')
            self.populate_fields = self.populate_fields + kwargs.pop('populate', [])
            logger.debug(f'Populate fields updated with populate fields', populate_fields=self.populate_fields)
        if 'exclude' in kwargs_args:
            logger.debug(f'Exclude fields found in kwargs, updating excluded fields')
            self.excluded_fields = self.excluded_fields + kwargs.pop('exclude', [])
            logger.debug(f'Excluded fields updated with exclude fields', excluded_fields=self.excluded_fields)

        if kwargs_args.get('context') and 'request' in kwargs_args.get('context'):
            logger.debug(f'Context found in kwargs, parsing fields from request')
            sf = self.parse_request_fields(kwargs, 'fields')
            pf = self.parse_request_fields(kwargs, 'populate')
            ex = self.parse_request_fields(kwargs, 'exclude')
            self.selected_fields = self.selected_fields + sf if sf is not None else self.selected_fields
            self.populate_fields = self.populate_fields + pf if pf is not None else self.populate_fields
            self.excluded_fields = self.excluded_fields + ex if ex is not None else self.excluded_fields
            logger.debug(f'Fields parsed from request', selected_fields=self.selected_fields, populate_fields=self.populate_fields,
                         excluded_fields=self.excluded_fields)
            self.selected_hierarchy = self.selected_hierarchy or self.build_hierarchy(self.selected_fields)
            self.populate_hierarchy = self.populate_hierarchy or self.build_hierarchy(self.populate_fields)
            self.exclude_hierarchy = self.exclude_hierarchy or self.build_hierarchy(self.excluded_fields)
        self.populate_fields = [
            field
            for field in self.populate_fields
            if field in self.model_fields_names and field not in self.excluded_fields
        ]
        self.selected_fields = [
            field for field in self.selected_fields
            if field in self.model_fields_names and field not in self.excluded_fields + self.populate_fields
        ]

        # fuse populate serializers
        self.populate_serializers = {**self.global_populate_serializers, **self.populate_serializers}

        # add generic relations names to Meta fields array
        if hasattr(self, 'Meta') and hasattr(self.Meta, 'model'):
            logger.debug(f'Adding generic relations to Meta fields')
            if self.Meta.fields == '__all__':
                logger.debug(f'All fields selected in Meta, updating Meta fields with model fields')
                self.Meta.fields = [field.name for field in self.Meta.model._meta.get_fields() if field.concrete]
            self.Meta.fields = list(self.Meta.fields) + list(self.generic_relations_names)
        logger.debug(f'calling super constructor of serializer {self.__class__.__name__}',
                     selected_fields=self.selected_fields, populate_fields=self.populate_fields, excluded_fields=self.excluded_fields)
        super().__init__(*args, **kwargs)

    def get_serializer_class(self, serializer_string: str):
        request = self.context.get('request', None)
        logger = getattr(request, 'logger', app_logger) if request else app_logger
        logger.debug(f'Getting serializer class for {serializer_string}')
        app_name, serializer_name = serializer_string.split('.')
        module_path = f'{app_name}.serializers'
        try:
            module = import_module(module_path)
            serializer_class = getattr(module, serializer_name)
            if issubclass(serializer_class, serializers.Serializer):
                logger.debug(f"Serializer '{serializer_string}' found and is a valid serializer class {serializer_class.__class__}")
                return serializer_class
            else:
                logger.warning(f"Serializer '{serializer_string}' is not a subclass of DRF Serializer")
                return None
        except (ImportError, AttributeError):
            logger.warning(f"Serializer '{serializer_string}' not found or not a valid serializer class.")
            return None

    def get_field_names(self, declared_fields, info):
        # exclude fields that are not in the model
        self.selected_fields = [field for field in self.selected_fields if field in self.model_fields_names]
        result = [field for field in self.selected_fields if field in {**info.fields, **info.forward_relations}]
        result.append('id')
        return result if len(result) > 1 else super().get_field_names(declared_fields, info)

    def to_representation(self, instance):
        request = self.context.get('request', None)
        logger = getattr(request, 'logger', app_logger) if request else self.context.get('logger', app_logger)
        logger.debug(f'Converting instance to representation for serializer {self.__class__.__name__}')
        self.selected_hierarchy = self.selected_hierarchy or self.build_hierarchy(set(self.selected_fields + self.populate_fields))
        self.populate_hierarchy = self.populate_hierarchy or self.build_hierarchy(self.populate_fields)
        result = OrderedDict()
        result['id'] = instance.id if hasattr(instance, 'id') else None
        primitive_fields = [
            field_name for field_name in self.fields
            if field_name not in self.relation_fields_names and field_name not in self.file_fields_names
        ]
        logger.debug(f'Primitive fields processed in serializer', primitive_fields=primitive_fields, selected_fields=self.selected_fields,
                     excluded_fields=self.excluded_fields)
        for field_name in self.fields:
            if getattr(instance, field_name, None) is None:
                result[field_name] = None
                continue
            if self.selected_fields and field_name not in self.selected_fields:
                continue
            if field_name in self.excluded_fields:
                continue
            if field_name in primitive_fields:
                result[field_name] = getattr(instance, field_name, None)
            if field_name in self.relation_fields_names:
                result[field_name] = getattr(instance, field_name, None)
                # apply to_representation
                if field_name in result and result[field_name]:
                    result[field_name] = self.fields[field_name].to_representation(result[field_name])
                else:
                    result[field_name] = None
            if field_name in self.file_fields_names:
                f = [f for f in self.file_fields if f.name == field_name and f.many]
                if f:
                    files = getattr(instance, field_name).all() if getattr(instance, field_name) else []
                    result[field_name] = [file.id for file in files]
                else:
                    file = getattr(instance, field_name).first() if getattr(instance, field_name) else None
                    result[field_name] = file.id if file else None
        logger.debug(f'Populate fields processed in serializer', populate_fields=self.populate_fields)
        for field_name in self.populate_fields:
            if getattr(instance, field_name, None) is None and field_name in self.populate_hierarchy:
                result[field_name] = None
                continue
            if field_name in self.populate_serializers and field_name in self.model_fields_names:
                serializer = self.get_serializer_class(self.populate_serializers[field_name])
                if serializer:
                    sh = self.selected_hierarchy.get(field_name, {}).copy()
                    ph = self.populate_hierarchy.get(field_name, {}).copy()
                    eh = self.exclude_hierarchy.get(field_name, {}).copy()
                    instance_data = None
                    if field_name in self.relation_fields_names:
                        instance_data = getattr(instance, field_name)
                    if field_name in self.file_fields_names:
                        if [f for f in self.file_fields if f.name == field_name and f.many]:
                            instance_data = list(getattr(instance, field_name).all() if getattr(instance, field_name) else [])
                        else:
                            instance_data = getattr(instance, field_name).first() if getattr(instance, field_name) else None
                    if not instance_data:
                        result[field_name] = None
                    else:
                        logger.debug(f'Populating field {field_name} with serializer {serializer.__class__.__name__}')
                        result[field_name] = serializer(
                            instance_data,
                            selected_hierarchy=sh,
                            populate_hierarchy=ph,
                            exclude_hierarchy=eh,
                            context={'logger': logger},
                            many=isinstance(instance_data, list)
                        ).data
        return result

    def build_hierarchy(self, field_paths):
        hierarchy = {}
        for path in field_paths:
            components = path.split('__')
            current_dict = hierarchy
            for component in components:
                if component not in current_dict:
                    current_dict[component] = {}
                current_dict = current_dict[component]
        return hierarchy
