from rest_framework import serializers
from .models import Variety

class VarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Variety
        fields = '__all__'