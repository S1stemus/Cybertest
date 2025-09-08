from models.models import Answer
from rest_framework import serializers

class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('name', 'is_correct')