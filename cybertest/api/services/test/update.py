from functools import lru_cache
from service_objects.services import ServiceWithResult
from models.models import Test, User
from service_objects.fields import ModelField
from django import forms
from service_objects.errors import NotFound


class TestUpdateService(ServiceWithResult):
    current_user = ModelField(User, required=True)
    test_id = forms.IntegerField( min_value=1)
    name = forms.CharField(max_length=127, required=False)

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_test
        return self

    @property
    def _update_test(self):
        test = Test.objects.get(id=self.cleaned_data["test_id"])
        test.name = self.cleaned_data["name"]
        test.save()
        return test
    @property
    @lru_cache
    def _test(self):
        try:
            return Test.objects.get(id=self.cleaned_data["test_id"])
        except Test.DoesNotExist:
            return None
    def _validate_test_id(self):
        if self._test is None:
            self.add_error("test_id", NotFound(message=f"Тест с id {self.cleaned_data['test_id']} не найден"))
    def _validated_user(self):
        if self.cleaned_data["current_user"].id != self._test.user.id:
            self.add_error(
                "current_user",
                NotFound(
                    message=f'пользователь {self.cleaned_data["current_user"]} не может удалить этот тест'
                ),
            )
    