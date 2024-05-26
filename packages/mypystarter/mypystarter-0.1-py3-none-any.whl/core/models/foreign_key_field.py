from django.contrib.contenttypes.fields import GenericRelation


class FileForeignKey(GenericRelation):
    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to') if 'upload_to' in kwargs else None
        self.field_name = kwargs.pop('field_name') if 'field_name' in kwargs else None
        self.many = kwargs.pop('many', False) if 'many' in kwargs else False
        super().__init__(*args, **kwargs)

    def get_default(self):
        return None
