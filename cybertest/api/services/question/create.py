from service_objects.services import ServiceWithResult
from models.models import Question, Test, User
from django import forms
from service_objects.errors import NotFound
from service_objects.fields import ModelField

class CreateQuestionService(ServiceWithResult):
    name = forms.CharField(max_length=127, required=True)
    test = forms.IntegerField(required=True, min_value=1)
    current_user = ModelField(User, required = True)

    def process(self) -> "ServiceWithResult":
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._create_question
        return self
    
    @property
    def _create_question(self):
        question = Question.objects.create(
            name = self.cleaned_data["name"],
            test = Test.objects.get(id = self.cleaned_data["test"]),
            user = self.cleaned_data["current_user"]                                    
        )
        return question
    
    def _validate_test(self):
        if not Test.objects.filter(id=self.cleaned_data["test"]).exists():
            self.add_error("test", NotFound(message=f"Тест с id {self.cleaned_data['test']} не найден"))

        