from models.models import Answer
from rest_framework import serializers

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('name', 'is_correct', 'question')