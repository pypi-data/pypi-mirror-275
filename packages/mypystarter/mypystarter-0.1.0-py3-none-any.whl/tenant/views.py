from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from mypystarter.mixins.create_form_data import CreateFormDataMixin
from mypystarter.mixins.create_json import CreateJsonMixin
from mypystarter.mixins.generic_view import GenericView
from mypystarter.mixins.handle_upload_file import FileFieldHandleMixin
from mypystarter.mixins.list import ListMixin
from mypystarter.mixins.soft_archive import SoftArchiveMixin
from mypystarter.mixins.update_form_data import UpdateFormDataMixin
from mypystarter.models import City
from mypystarter.serializers.upload import UploadSerializer
from tenant.models import Product
from tenant.serializers import ProductSerializer, CitySerializer, ProductMutationUpdateSerializer


class FileFieldCRUDView(FileFieldHandleMixin):
    @action(detail=True, methods=['post'], url_name='img')
    @swagger_auto_schema(request_body=UploadSerializer, manual_parameters=UploadSerializer.get_file_param())
    def img(self, request, pk, *args, **kwargs):
        return self.upload_single_file('img', ProductSerializer)


class ProductView(SoftArchiveMixin, UpdateFormDataMixin, ListMixin, CreateFormDataMixin, FileFieldCRUDView, GenericView):
    queryset = Product.objects.all().order_by('-id')
    all_queryset = Product.all_objects.all().order_by('-id')
    search_fields = ['name', 'id']
    filterset = ['name', 'id', 'img2__size', 'client__id', 'client__name']
    ordering_fields = ['name', 'id', 'client__id', 'client__name', 'img2__size']
    serializer_class = ProductSerializer
    serializer_action_classes_per_version = {
        '1': {
            'create': ProductMutationUpdateSerializer,
            'partial_update': ProductMutationUpdateSerializer,
        }
    }


class CityView(ListMixin, CreateJsonMixin, GenericViewSet):
    queryset = City.objects.all().order_by('-id')
    serializer_class = CitySerializer
    search_fields = ['name', 'id']
    filterset = ['name', 'id']
    ordering_fields = ['name', 'id']
