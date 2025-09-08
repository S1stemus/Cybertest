
from models.models import Question
from rest_framework import serializers
from api.serializers.test.show import TestShowSerializer
from api.serializers.user_answer.show import UserAnswerShowSerializer
from api.serializers.user.show import UserSerializer


class QuestionListSerializer(serializers.ModelSerializer):
    test = TestShowSerializer()
    user_answers = UserAnswerShowSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Question
        fields = ["id", "name", "test", "user_answers", "user"]