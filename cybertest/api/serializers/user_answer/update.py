
from models.models import UserAnswer
from rest_framework import serializers

class UserAnswerUpdateSerializer(serializers.ModelSerializer):
    answer_id = serializers.IntegerField()
    class Meta:
        model = UserAnswer
        fields = ["answer_id"]