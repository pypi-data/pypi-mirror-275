from mypystarter.models import AppUser, Client, City, Country
from mypystarter.serializers.create import MutationSerializer
from mypystarter.serializers.read import ReadSerializer
from tenant.models import Product


class ProductMutationUpdateSerializer(MutationSerializer):
    creation_fields = ['client', 'img', 'name', 'img2']
    populate_serializers = {
        'img': 'mypystarter.PrivateFileSerializer',
        'img2': 'mypystarter.PrivateFileSerializer',
        'client': 'tenant.ClientSerializer',
        'clients': 'tenant.ClientSerializer',
    }

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(ReadSerializer):
    populate_serializers = {
        'img': 'mypystarter.PrivateFileSerializer',
        'img2': 'mypystarter.PrivateFileSerializer',
        'client': 'tenant.ClientSerializer',
        'clients': 'tenant.ClientSerializer'
    }
    populate_fields = []
    generic_relations_names = ['img']

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(ReadSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class ClientSerializer(ReadSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CountrySerializer(ReadSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(ReadSerializer):
    class Meta:
        model = City
        fields = '__all__'
