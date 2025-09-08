from models.models import Test
from rest_framework import serializers

class TestShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["id", "name"]