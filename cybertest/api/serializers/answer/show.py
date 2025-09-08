from models.models import Answer
from rest_framework import serializers

class AnswerShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'question')