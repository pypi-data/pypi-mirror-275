from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from mypystarter.logger import app_logger
from mypystarter.models import PublicFile, File
from mypystarter.types import IRequest


class FileFieldHandleMixin(GenericViewSet):

    def __update_file(self, file_obj: File, file: InMemoryUploadedFile) -> File:
        request: IRequest = self.request
        logger = getattr(request, 'logger', app_logger)
        if not file_obj:
            logger.error(f'received None for file object when requesting file update, skipping update of file details')
            return file_obj
        logger.info(f'Updating file details for file #{file_obj.id}')
        if file:
            logger.debug(f'Updating file #{file_obj.id} details with new uploaded file {file.name}')
            file_obj.file = file
            file_obj.filename = file.name
            file_obj.size = file.size
            file_obj.mime_type = file.content_type
            file_obj.title = self.request.data.get('title', file.name)
        else:
            logger.error(f'file not found in request files, skipping update of file details')
        file_obj.description = self.request.data.get('description')
        file_obj.is_public = self.request.data.get('is_public', isinstance(file_obj, PublicFile))
        logger.info(f'File details updated for file #{file_obj.id}')
        return file_obj

    def upload_single_file(self, field_name: str, serializer_class: Serializer.__class__ = Serializer):
        request: IRequest = self.request
        logger = getattr(request, 'logger', app_logger)
        instance: Model = self.get_object()
        logger.info(f'Uploading single file for field {field_name} for object {instance}')
        file = self.request.data.get('file')
        file_attr = getattr(instance, field_name)
        if file_attr:
            logger.debug(f'File attribute found for field {field_name}')
            file_obj = file_attr.first()
            model = file_attr.model
            if file_obj:
                logger.debug(f'File object found for field {field_name}')
                file_obj = self.__update_file(file_obj, file)
                file_obj.save()
            else:
                logger.debug(f'No file object found for field {field_name}, creating new file object')
                model.objects.create(
                    file=file,
                    filename=file.name,
                    size=file.size,
                    mime_type=file.content_type,
                    description=self.request.data.get('description'),
                    title=self.request.data.get('title', file.name),
                    is_public=self.request.data.get('is_public', isinstance(file_attr.model, PublicFile)),
                    content_object=instance
                )
        logger.info(f'File uploaded for field {field_name} for object {instance}, refreshing object from db')
        instance.refresh_from_db()
        serializer = serializer_class(instance, context={'request': self.request})
        logger.info(f'File uploaded successfully for field {field_name} for object {instance}')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_single_file(self, field_name: str, serializer_class: Serializer.__class__ = Serializer):
        request: IRequest = self.request
        logger = getattr(request, 'logger', app_logger)
        instance: Model = self.get_object()
        logger.info(f'Deleting single file for field {field_name} for object {instance}')
        file_attr = getattr(instance, field_name)
        if file_attr:
            logger.debug(f'File attribute found for field {field_name}')
            file_obj = file_attr.first()
            if file_obj:
                logger.debug(f'File object found for field {field_name}')
                logger.info(f'Deleting file object for field {field_name} for object {instance}')
                file_obj.delete()
                logger.info(f'File deleted for field {field_name} for object {instance}, refreshing object from db')
            else:
                logger.warning(f'No file object found for field {field_name}, skipping delete')
        else:
            logger.warning(f'No file attribute found for field {field_name}, skipping delete')
        instance.refresh_from_db()
        serializer = serializer_class(instance, context={'request': self.request})
        logger.info(f'Operation finished successfully for field {field_name} for object {instance}')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def add_multiple_file(self, field_name: str, serializer_class: Serializer.__class__ = Serializer):
        instance = self.get_object()
        request: IRequest = self.request
        logger = getattr(request, 'logger', app_logger)
        logger.info(f'Adding multiple files for field {field_name} for object {instance}')
        file = self.request.data.get('file')
        files = self.request.FILES.getlist('files', [])
        file_attr = getattr(instance, field_name)
        if file:
            logger.debug(f'File found in request data, adding file to files list')
            files.append(file)
        model = file_attr.model
        logger.info(f'Creating {len(files)} file(s) for field {field_name} for object {instance}')
        for file in files:
            model.objects.create(
                file=file,
                filename=file.name,
                size=file.size,
                mime_type=file.content_type,
                description=self.request.data.get('description'),
                title=self.request.data.get('title', file.name),
                is_public=self.request.data.get('is_public', isinstance(file_attr.model, PublicFile)),
                content_object=instance
            )
        logger.info(f'Files created for field {field_name} for object {instance}, refreshing object from db')
        instance.refresh_from_db()
        serializer = serializer_class(instance, context={'request': self.request})
        logger.info(f'Files created successfully for field {field_name} for object {instance}')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_multiple_file(self, field_name: str, file_id: int, serializer_class=Serializer):
        instance = self.get_object()
        request: IRequest = self.request
        logger = getattr(request, 'logger', app_logger)
        logger.info(f'Deleting a file from a multi-files field {field_name} for object {instance}')
        file_attr = getattr(instance, field_name)
        file_obj = file_attr.filter(id=file_id).first()
        if file_obj:
            logger.debug(f'File object found for field {field_name}')
            logger.info(f'Deleting file object for field {field_name} for object {instance}')
            file_obj.delete()
        else:
            logger.warning(f'No file object found for field {field_name}, skipping delete and refreshing object from db')
        instance.refresh_from_db()
        serializer = serializer_class(instance, context={'request': self.request})
        logger.info(f'File deleted successfully for file #{file_id} for field {field_name} for object {instance}')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_multiple_file(self, field_name, file_id, serializer_class=Serializer):
        request: IRequest = self.request
        logger = request.logger
        instance = self.get_object()
        logger.info(f'Updating file #{file_id} for multi-files field {field_name} for object {instance} ')
        file_attr = getattr(instance, field_name)
        file_obj = file_attr.filter(id=file_id).first()
        if file_obj:
            logger.debug(f'File #{file_id} found. proceeding to update')
            file = self.request.data.get('file', None)
            if file_obj.file:
                logger.info(f'Designated file #{file_id} have already a file, deleting old file ')
                file_obj.file.delete()
            else:
                logger.info(f'Designated file #{file_id} doesnt have already a file')
            file_obj = self.__update_file(file_obj, file)
            file_obj.save()
        else:
            logger.warning(f'File #{file_id} not found, add a new file')
            return self.add_multiple_file(field_name, serializer_class)
        instance.refresh_from_db()
        serializer = serializer_class(instance, context={'request': self.request})
        logger.info(f'Operation Finished successfully for multi-files field {field_name} for object {instance}', serializer=serializer.__class__)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def clear_multiple_file(self, field_name: str, serializer_class=Serializer):
        request: IRequest = self.request
        logger = request.logger
        instance = self.get_object()
        logger.info(f'Clearing all files for multi-files field {field_name} for object {instance}')
        file_attr = getattr(instance, field_name)
        if file_attr:
            logger.debug(f'File attribute found for field {field_name}')
            for file_obj in file_attr.all():
                logger.debug(f'Deleting file #{file_obj.id} for field {field_name} for object {instance}')
                file_obj.delete()
        else:
            logger.warning(f'No file attribute found for field {field_name}, skipping delete')
        instance.refresh_from_db()
        serializer = serializer_class(instance, context={'request': self.request})
        logger.info(f'Operation Finished successfully for multi-files field {field_name} for object {instance}', serializer=serializer.__class__)
        return Response(serializer.data, status=status.HTTP_200_OK)
