from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class QuestionDeleteService(ServiceWithResult):
    question_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User, required=True)

    custom_validations = ["_validate_id"]
    def process(self) -> "ServiceWithResult":
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete_question
        return self

    @property
    def _delete_question(self):
        question = Question.objects.get(id=self.cleaned_data["question_id"])
        question.delete()
    def _validate_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))
    def _validated_user(self):
        if self.cleaned_data["current_user"].id != Question.objects.get(id=self.cleaned_data["question_id"]).test.user.id:
            self.add_error("current_user", NotFound(message=f'пользователь {self.cleaned_data["current_user"]} не может удалить этот вопрос'))

    