from rest_framework import serializers
from .models import About, ExtraData

class ExtraDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraData
        fields = ['title', 'description']

class AboutSerializer(serializers.ModelSerializer):
    extra_data = ExtraDataSerializer(many=True)

    class Meta:
        model = About
        fields = ['title', 'extra_data']

    def create(self, validated_data):
        extra_data_data = validated_data.pop('extra_data')
        about_instance = About.objects.create(**validated_data)

        for extra_data in extra_data_data:
            extra_data_instance = ExtraData.objects.create(**extra_data)
            about_instance.extra_data.add(extra_data_instance)

        return about_instance

    def update(self, instance, validated_data):
        extra_data_data = validated_data.pop('extra_data')
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        instance.extra_data.clear()
        for extra_data in extra_data_data:
            extra_data_instance = ExtraData.objects.create(**extra_data)
            instance.extra_data.add(extra_data_instance)

        return instance
