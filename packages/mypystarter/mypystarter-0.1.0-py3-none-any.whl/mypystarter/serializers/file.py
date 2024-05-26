from mypystarter.models import PrivateFile, PublicFile
from mypystarter.serializers.read import ReadSerializer


class PrivateFileSerializer(ReadSerializer):
    class Meta:
        model = PrivateFile
        fields = '__all__'

    def to_representation(self, attrs):
        attrs = super().to_representation(attrs)
        attrs['file'] = attrs['file'].url
        return attrs


class PublicFileSerializer(ReadSerializer):
    class Meta:
        model = PublicFile
        fields = '__all__'

    def to_representation(self, attrs):
        attrs = super().to_representation(attrs)
        attrs['file'] = attrs['file'].url
        return attrs
