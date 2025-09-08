from models.models import Question
from rest_framework import serializers
from api.serializers.test.show import TestShowSerializer
from api.serializers.answer.show import AnswerShowSerializer
from api.serializers.user_answer.show import UserAnswerShowSerializer


class QuestionShowSerializer(serializers.ModelSerializer):
    answers = AnswerShowSerializer(many=True)
    user_answers = UserAnswerShowSerializer(many=True)
    class Meta:
        model = Question
        fields = ["id", "name", "answers","user_answers"]