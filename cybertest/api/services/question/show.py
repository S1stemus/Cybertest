from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class QuestionShowService(ServiceWithResult):
    question_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User, required = False)

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._question
        return self
    @property
    def _question(self):
        try:
            question = (
                Question.objects.filter(id=self.cleaned_data["question_id"])
                    .prefetch_related(
                        Prefetch(
                        'user_answers',
                        queryset=UserAnswer.objects.filter(user=self.cleaned_data["current_user"])
                    ))
                    .prefetch_related('answers')            
                )
        except Question.DoesNotExist:
            return None
        return question
    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))