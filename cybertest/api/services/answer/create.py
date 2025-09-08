from service_objects.services import ServiceWithResult

from models.models import Question, Test, UserAnswer, User,Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class AnswerCreateService(ServiceWithResult):
    question = forms.IntegerField()
    current_user = ModelField(User, required=True)
    is_correct = forms.IntegerField(required=True)
    name = forms.CharField(max_length=127, required=True)


    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._create_answer
        return self

    @property
    def _create_answer(self):
        print(self.cleaned_data["is_correct"])
        question = Question.objects.get(id=self.cleaned_data["question"])
        answer = Answer.objects.create(name=self.cleaned_data["name"], is_correct=self.cleaned_data["is_correct"], question=question, user=self.cleaned_data["current_user"])
        return answer
    
    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))
        