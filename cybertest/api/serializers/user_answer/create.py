from models.models import UserAnswer
from rest_framework import serializers

class UserAnswerCreateSerializer(serializers.ModelSerializer):
    answer_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    class Meta:
        model = UserAnswer
        fields = ["answer_id", "question_id"]