from service_objects.services import ServiceWithResult
from models.models import Question, UserAnswer, User, Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField


class CreateUserAnswerService(ServiceWithResult):
    current_user = ModelField(User, required = True)
    answer_id = forms.IntegerField(required=True, min_value=1)
    question_id = forms.IntegerField(required=True, min_value=1)

    custom_validations = ["_validate_question_id", "_validate_answer_id"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._create_user_answer        
        return self
    
    @property
    def _create_user_answer(self):
        question = Question.objects.get(id=self.cleaned_data["question_id"])
        answer = Answer.objects.get(id=self.cleaned_data["answer_id"])
        answer.choices += 1
        answer.save()
        user_answer = UserAnswer.objects.create(user=self.cleaned_data["current_user"], question=question, answer=answer, is_correct_answer=answer.is_correct)
        return user_answer
    
    def _validate_question_id(self):
        if not Question.objects.filter(id=self.cleaned_data["question_id"]).exists():
            self.add_error("question_id", NotFound(message=f"Вопрос с id {self.cleaned_data['question_id']} не найден"))

    def _validate_answer_id(self):
        if not Answer.objects.filter(id=self.cleaned_data["answer_id"]).exists():
            self.add_error("answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['answer_id']} не найден"))