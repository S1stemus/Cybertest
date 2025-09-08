from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User,Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField
from django.db.models import Count
from django.db.models import Q

class UserAnswerDeleteService(ServiceWithResult):
    user_answer_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User, required = True)
    custom_validations = ["_validate_user_answer_id", "_validated_user"]
    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete_user_answer
        return self
    @property
    def _delete_user_answer(self):
        user_answer = UserAnswer.objects.get(id=self.cleaned_data["user_answer_id"])
        user_answer.delete()


    def _validate_user_answer_id(self):
        if not UserAnswer.objects.filter(id=self.cleaned_data["user_answer_id"]).exists():
            self.add_error("user_answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['user_answer_id']} не найден"))
    def _validated_user(self):
        if self.cleaned_data["current_user"].id != UserAnswer.objects.get(id=self.cleaned_data["user_answer_id"]).user.id:
            self.add_error("current_user", NotFound(message=f'пользователь {self.cleaned_data["current_user"]} не может удалить этот ответ')) 