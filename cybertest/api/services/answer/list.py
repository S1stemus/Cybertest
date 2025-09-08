from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User,Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField


class AnswerListService(ServiceWithResult):
    question_id = forms.IntegerField(required=True, min_value=1)

    custom_validations = ["_validate_question_id"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._answers
        return self

    @property
    def _answers(self):
        answers = Answer.objects.filter(question=self.cleaned_data["question_id"])
        print(answers)
        return answers
    

    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))