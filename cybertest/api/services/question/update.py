from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class QuestionUpdateService(ServiceWithResult):
    question_id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=127, required=True)
    current_user = ModelField(User, required = True)

    custom_validations = ["_validate_question_id", "_validated_user"]

    def process(self) -> ServiceWithResult:
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_question
        return self

    @property
    def _update_question(self):
        question = Question.objects.get(id = self.cleaned_data["question_id"])
        question.name = self.cleaned_data["name"]
        question.save()
        return question
    def _validate_question_id(self):
        if not Question.objects.filter(id = self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))
    def _validated_user(self):
        if self.cleaned_data["current_user"].id != Question.objects.get(id=self.cleaned_data["question_id"]).user.id:
            print(self.cleaned_data["current_user"])
            self.add_error("current_user", NotFound(message=f'пользователь {self.cleaned_data["current_user"]} не может изменить этот вопрос'))