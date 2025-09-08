from models.models import Test
from rest_framework import serializers

class TestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["name"]