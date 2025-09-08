from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField

class QuestionListByTestIdService(ServiceWithResult):
    current_user = ModelField(User, required = False)
    test_id = forms.IntegerField(required=True, min_value=1)
    custom_validations = ["_validate_test_id"]

    def process(self) -> "ServiceWithResult":
        self.run_custom_validations()
        self.result = self._questions
        return self
    
    @property
    def _questions(self):
        try:
            questions = (Question.objects.filter(test=self.cleaned_data["test_id"])
            .select_related('test').
            prefetch_related(
                Prefetch(
                    'user_answers',
                    queryset=UserAnswer.objects.filter(user=self.cleaned_data["current_user"])
                ))
            )

            return questions
        except Question.DoesNotExist:
            return None
    def _validate_test_id(self):
        if  Test.objects.filter(id=self.cleaned_data["test_id"]).exists() == False:
            self.add_error("test_id", NotFound(message=f"Тест с id {self.cleaned_data['test_id']} не найден"))
            print(self.errors)