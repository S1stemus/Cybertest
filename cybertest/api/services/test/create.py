from service_objects.services import ServiceWithResult
from models.models import Test, User
from django import forms
from service_objects.fields import ModelField

class TestCreateService(ServiceWithResult):
    name = forms.CharField(max_length=127, required=True)
    current_user = ModelField(User, required = True)

    def process(self) -> "ServiceWithResult":
        self.result = self._create_test
        return self
    
    @property
    def _create_test(self):
        test = Test.objects.create(name=self.cleaned_data["name"])   
        test.user.set([self.cleaned_data["current_user"]])     
        return test
