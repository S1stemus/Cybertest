from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User,Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class AnswerUpdateService(ServiceWithResult):

    answer_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User)
    is_correct = forms.IntegerField()
    name = forms.CharField(max_length=127)

    custom_validations = ["_validate_answer_id", "_validated_user"]
    
    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_answer
        return self
    @property    
    def _update_answer(self):
        answer = Answer.objects.get(id=self.cleaned_data["answer_id"])
        answer.is_correct = self.cleaned_data["is_correct"]
        answer.name = self.cleaned_data["name"]
        answer.save()
        return answer
    def _validate_answer_id(self):
        if not Answer.objects.filter(id=self.cleaned_data["answer_id"]).exists():
            self.add_error("answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['answer_id']} не найден"))
    def _validated_user(self):
        if self.cleaned_data["current_user"].id != Answer.objects.get(id=self.cleaned_data["answer_id"]).user.id:
            self.add_error("current_user", NotFound(message=f'пользователь {self.cleaned_data["current_user"]} не может обновить этот ответ'))