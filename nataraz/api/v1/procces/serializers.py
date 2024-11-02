from rest_framework import serializers
from .models import Process

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['step', 'title', 'subtitle', 'description']

    def validate_step(self, value):
        if value < 0:
            raise serializers.ValidationError("Step not negative number.")
        return value
