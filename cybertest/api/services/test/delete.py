from functools import lru_cache
from service_objects.services import ServiceWithResult
from models.models import Test, User
from service_objects.fields import ModelField
from django import forms
from service_objects.errors import NotFound

class TestDeleteService(ServiceWithResult):
    
    test_id = forms.IntegerField( min_value=1)
    current_user = ModelField(User)
    custom_validations = ["_validate_test_id", "_validated_user"]
    def process(self):
        self.result = self._delete_test
        return self
    @property
    def _delete_test(self):
        test = Test.objects.get(id=self.cleaned_data["test_id"])
        test.delete()
    
    def _validate_test_id(self):
        if not Test.objects.filter(id=self.cleaned_data["test_id"]).exists():
            self.add_error("test_id", NotFound(message=f"Тест с id {self.cleaned_data['test_id']} не найден"))

    def _validated_user(self):
        if self.cleaned_data["current_user"].id != Test.objects.get(id=self.cleaned_data["test_id"]).user.id:
            self.add_error("current_user", NotFound(message=f'пользователь {self.cleaned_data["current_user"]} не может удалить этот тест'))