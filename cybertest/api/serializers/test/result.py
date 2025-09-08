from models.models import Test
from rest_framework import serializers

class TestresultSerializer(serializers.ModelSerializer):
    result = serializers.IntegerField(read_only=True)
    class Meta:
        model = Test
        fields = ["id", "name",'result']