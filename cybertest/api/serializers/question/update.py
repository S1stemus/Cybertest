from models.models import Question
from rest_framework import serializers
from api.serializers.test.show import TestShowSerializer
from api.serializers.user_answer.show import UserAnswerShowSerializer


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["name"]