from service_objects.services import ServiceWithResult
from models.models import Question, Test, UserAnswer, User,Answer
from django import forms
from service_objects.errors import NotFound
from django.db.models import Prefetch
from service_objects.fields import ModelField
from django.db.models import Count
from django.db.models import Q

class ResultService(ServiceWithResult):
    current_user = ModelField(User, required = True)
    test_id = forms.IntegerField(required=True, min_value=1)
    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._result
        return self
    @property
    def _result(self):
        return (
            Test.objects.filter(id=self.cleaned_data["test_id"])
            .annotate(result=Count("user_answer", filter=
                                 Q(user_answer__user=self.cleaned_data["current_user"]) &
                                 Q(user_answer__is_correct_answer=1) &
                                Q(user_answer__test=self.cleaned_data["test_id"])
                                ))
            
        )
    
    def _validate_test_id(self):
        if self._result is None:
            self.add_error("test_id", NotFound(message=f"Тест с id {self.cleaned_data['test_id']} не найден"))
    
    