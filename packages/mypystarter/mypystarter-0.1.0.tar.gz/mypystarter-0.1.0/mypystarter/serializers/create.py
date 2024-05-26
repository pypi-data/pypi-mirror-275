from django.db.models import Model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mypystarter.logger import app_logger


class MutationSerializer(ModelSerializer):
    creation_fields = []
    populate_serializers = {}
    file_fields = []
    many_to_many_fields = []
    file_fields_names = [f.name for f in file_fields]

    def __init__(self, *args, **kwargs):
        context: dict = kwargs.get('context', {})
        request = context.get('request') if context else None
        logger = getattr(request, 'logger', None) if request else None
        view = context.get('view') if context else None
        super().__init__(*args, **kwargs)
        # noinspection PyProtectedMember
        fields = self.Meta.model._meta.get_fields()
        self.file_fields = [
            field
            for field in fields
            if field.related_model and field.related_model.__name__ in ['PrivateFile', 'PublicFile']
        ]
        self.many_to_many_fields = [
            field
            for field in fields
            if field.many_to_many
        ]
        for field in self.file_fields:
            request = kwargs.get('context').get('request')
            if request.accepted_media_type == 'application/openapi+json':
                self.fields[field.name] = serializers.FileField()
            else:
                if field.many:
                    self.fields[field.name] = serializers.ListField(child=serializers.FileField())
                else:
                    self.fields[field.name] = serializers.FileField()
            self.fields[field.name].required = not field.null
        if view:
            if hasattr(view, 'swagger_fake_view') and view.swagger_fake_view:
                self.Meta.fields = self.creation_fields
        logger.debug(f'calling constructor of serializer {self.__class__.__name__}',
                     fields=self.file_fields_names, many_to_many_fields=[f.name for f in self.many_to_many_fields])

    class Meta:
        model = None
        fields = None

    def create(self, validated_data):
        request = self.context.get('request', None)
        logger = getattr(request, 'logger', app_logger) if request else app_logger
        logger.info(f'Creating object with serializer {self.__class__.__name__}', validated_data=validated_data)
        logger.debug(f'Processing Many to Many fields for object creation', many_to_many_fields=[f.name for f in self.many_to_many_fields])
        # handle many to many fields
        many_to_many_data = {}
        for field in self.many_to_many_fields:
            if field.name in validated_data:
                many_to_many_data[field.name] = validated_data.pop(field.name)
        logger.debug(f'File fields for object creation are {self.file_fields_names}')
        # handle file fields
        files_data = {}
        for field in self.file_fields:
            logger.debug(f'Processing file field {field.name} for object creation')
            if field.name in validated_data:
                files_data[field] = []
                f = validated_data[field.name]
                f = f if isinstance(f, list) else [f]
                for ff in f:
                    file_data = {
                        'many': field.many,
                        'upload_to': field.upload_to,
                        'field_name': field.name,
                        'size': ff.size,
                        'filename': ff.name,
                        'mime_type': ff.content_type,
                        'file': ff,
                    }
                    files_data[field] = files_data[field] + [file_data]
                validated_data.pop(field.name)
        logger.info(f'Creating object with serializer {self.__class__.__name__}', validated_data=validated_data)
        instance = self.Meta.model.objects.create(**validated_data)
        logger.debug(f'Object {instance} created successfully, saving file fields')
        # save file fields
        for field, file_data in files_data.items():
            for f_data in file_data:
                f_data['content_object'] = instance
                field.related_model.objects.create(**f_data)
        logger.debug(f'File fields saved successfully for object {instance}, saving many to many fields',
                     many_to_many_fields=many_to_many_data.keys())
        # save many to many fields
        for field, values in many_to_many_data.items():
            for value in values:
                getattr(instance, field).add(value)
        logger.info(f'Object {instance} created successfully with serializer {self.__class__.__name__}')
        return instance

    def validate(self, attrs):
        for field in self.file_fields:
            if field.name in attrs:
                f = attrs[field.name]
                f = f if isinstance(f, list) else [f]
                # attrs[field.name] = f
        return attrs

    def update(self, instance: Model, validated_data: dict) -> Model:
        request = self.context.get('request', None)
        logger = getattr(request, 'logger', app_logger) if request else app_logger
        logger.info(f'Updating object {instance} with serializer {self.__class__.__name__}', validated_data=validated_data)
        # handle many to many fields
        logger.debug(f'Processing Many to Many fields for object update', many_to_many_fields=[f.name for f in self.many_to_many_fields])
        for field in self.many_to_many_fields:
            if field.name in validated_data:
                existing_relations = getattr(instance, field.name)
                if existing_relations:
                    logger.debug(f'Removing existing relations for field {field.name} for object {instance}')
                    for relation in existing_relations.all():
                        getattr(instance, field.name).remove(relation)
                logger.debug(f'Adding new relations for field {field.name} for object {instance}')
                for value in validated_data[field.name]:
                    getattr(instance, field.name).add(value)
        logger.debug(f'File fields for object update', file_fields=self.file_fields_names)
        # ignore filefields and Remove file fields from validated data
        for file_field in self.file_fields:
            validated_data.pop(file_field.name, None)
        logger.info(f'Updating object {instance} with serializer {self.__class__.__name__}', validated_data=validated_data)
        # update other fields
        for f in validated_data:
            setattr(instance, f, validated_data[f])
        instance.save()
        logger.info(f'Object {instance} updated successfully with serializer {self.__class__.__name__}')
        return instance
