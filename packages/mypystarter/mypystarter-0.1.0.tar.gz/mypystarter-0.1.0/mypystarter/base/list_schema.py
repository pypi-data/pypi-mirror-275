from django.db.models import Model
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema


class ListCustomSchema(SwaggerAutoSchema):
    excluded_fields = ['password']

    def get_create_params(self, operation_keys=None):
        # read existing operation params and add new params
        params = super().get_operation(operation_keys)
        return [
            *params.get('parameters', []),
            *self.get_read_params(operation_keys),
        ]

    def get_read_params(self, operation_keys=None):
        relations_names = []
        fields_names = []
        if hasattr(self.view, 'queryset') and hasattr(self.view.queryset.model, '_meta'):
            model: Model = self.view.queryset.model
            relations_names = [field.name for field in model._meta.get_fields() if field.is_relation]
            fields = model._meta.get_fields()
            fields_names = [field.name for field in fields if field.name not in self.excluded_fields]
            fields_names.sort()
        params = [
            openapi.Parameter(
                name='fields',
                in_=openapi.IN_QUERY,
                description=f'Fields to be returned in the response. If not provided, all fields will be returned. \n'
                            f' Available fields : {" | ".join(fields_names)}',
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING)
            ),
            openapi.Parameter(
                name='exclude',
                in_=openapi.IN_QUERY,
                description=f'Fields to be excluded in the response. If provided with fields, exclude wins \n'
                            f' Available fields : {" | ".join(fields_names)}',
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING)
            ),
            openapi.Parameter(
                name='populate',
                in_=openapi.IN_QUERY,
                description=f'Fields to be populated in the response. If not provided, no fields will be populated. \n'
                            f' Available fields : {" | ".join(relations_names)}',
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING)
            )
        ]
        return params

    def get_group_ids_params(self, operation_keys=None):
        return [
            openapi.Parameter(
                name='ids',
                in_=openapi.IN_QUERY,
                description='List of IDs to be deleted',
                required=True,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER)
            )
        ]

    def get_list_params(self, operation_keys=None):
        params = self.get_read_params(operation_keys)
        if hasattr(self.view, 'filterset'):
            for f in self.view.filterset:
                params.append(openapi.Parameter(
                    name=f,
                    in_=openapi.IN_QUERY,
                    description='Filter Records  by {}'.format(f),
                    required=False,
                    type=openapi.TYPE_STRING
                ))
        if hasattr(self.view, 'search_fields'):
            params.append(openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Search Records using these fields : {}'.format(' | '.join(self.view.search_fields)),
                required=False,
                type=openapi.TYPE_STRING
            ))
        if hasattr(self.view, 'ordering_fields'):
            order_params = []
            for f in self.view.ordering_fields:
                order_params.append(f)
                order_params.append('-{}'.format(f))
            params.append(openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                description='Sort Records by these fields : {}'.format(' | '.join(self.view.ordering_fields)),
                required=False,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(enum=order_params, type=openapi.TYPE_STRING)
            ))
        params.append(openapi.Parameter(
            name='page',
            in_=openapi.IN_QUERY,
            description='Page Number',
            required=False,
            type=openapi.TYPE_INTEGER
        ))
        params.append(openapi.Parameter(
            name='page_size',
            in_=openapi.IN_QUERY,
            description='Page Size',
            required=False,
            type=openapi.TYPE_INTEGER
        ))
        return params

    def get_operation(self, operation_keys=None):
        operation = super().get_operation(operation_keys)
        params = {
            'create': self.get_create_params(operation_keys),
            'delete': self.get_create_params(operation_keys),
            'update': self.get_create_params(operation_keys),
            'partial_update': self.get_create_params(operation_keys),
            'read': self.get_read_params(operation_keys),
            'list': self.get_list_params(operation_keys),
            'deleted': self.get_list_params(operation_keys),
            'group_destroy': self.get_group_ids_params(operation_keys),
            'group_restore': self.get_group_ids_params(operation_keys),
            'group_soft_delete': self.get_group_ids_params(operation_keys),
            'archived': self.get_list_params(operation_keys),
            'retrieve_archived': self.get_read_params(operation_keys),
        }
        if operation_keys:
            op_params = params.get(operation_keys[-1])
            if op_params:
                operation['parameters'] = op_params
        return operation
