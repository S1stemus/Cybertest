from service_objects.services import ServiceWithResult
from models.models import Question, UserAnswer, User, Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class UpdateUserAnswerService(ServiceWithResult):
    user_answer_id = forms.IntegerField(required=True, min_value=1)
    answer_id = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User, required = True)

    custom_validations = ["_validate_user_answer_id", "_validate_answer_id", "_validate_user"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_answer
        return self


    @property
    def _update_answer(self):
        user_answer = UserAnswer.objects.get(id=self.cleaned_data["user_answer_id"])
        print(user_answer.answer.id)        
        prev_answer = Answer.objects.get(id = user_answer.answer.id)
        prev_answer.choices -= 1
        prev_answer.save()
        answer = Answer.objects.get(id=self.cleaned_data["answer_id"])
        answer.choices += 1
        answer.save()
        user_answer.answer = answer
        user_answer.save()
        return user_answer
    
    def _validate_answer_id(self):
        if not Answer.objects.filter(id=self.cleaned_data["answer_id"]).exists():
            self.add_error("answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['answer_id']} не найден"))

    def _validate_user_answer_id(self):
        if not UserAnswer.objects.filter(id=self.cleaned_data["user_answer_id"]).exists():
            self.add_error("user_answer_id", NotFound(message=f"Ответ с id {self.cleaned_data['user_answer_id']} не найден"))

    def _validate_user(self):
        if self.cleaned_data["current_user"] != UserAnswer.objects.get(id=self.cleaned_data["user_answer_id"]).user:
            self.add_error("user", "Вы не можете редактировать ответ другого пользователя")
    


    