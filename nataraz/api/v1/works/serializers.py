from rest_framework import serializers
from .models import Work, Contributor, ExtraData
from api.v1.services.models import Service
from rest_framework import serializers
from .models import Work, ExtraData, Image
from rest_framework import serializers
from .models import Work, ExtraData, Image
from api.v1.services.models import Service

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'file', 'image_type']

class ExtraDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraData
        fields = ['title', 'desc']

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['fullname']

class WorkSerializer(serializers.ModelSerializer):
    extra_data = ExtraDataSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Service.objects.all())
    contributor = serializers.SerializerMethodField()

    class Meta:
        model = Work
        fields = ['title', 'cover', 'video', 'category', 'date', 'contributor', 'extra_data', 'images']

    def get_contributor(self, obj):
        contributors = obj.contributor.all()
        return [ContributorSerializer(contributor).data for contributor in contributors]
