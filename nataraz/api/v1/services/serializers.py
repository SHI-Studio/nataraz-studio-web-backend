from rest_framework import serializers
from .models import Service, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ServiceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'tags']

    def validate_tags(self, value):
        if not value:
            raise serializers.ValidationError("At least one tag is required.")
        return value
