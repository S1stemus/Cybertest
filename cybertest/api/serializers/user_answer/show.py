
from models.models import UserAnswer
from rest_framework import serializers
from api.serializers.answer.show import AnswerShowSerializer
from api.serializers.user.show import UserSerializer

class UserAnswerShowSerializer(serializers.ModelSerializer):
    answer = AnswerShowSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserAnswer
        fields = ["id", "answer", "user", "question"]