from rest_framework import serializers
from .models import Member, ExtraData

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['title', 'position', 'image', 'linkedin_url']

class ExtraDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraData
        fields = ['title', 'description']
