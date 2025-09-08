from service_objects.services import ServiceWithResult
from models.models import Test


class TestListService(ServiceWithResult):

    def process(self) -> "ServiceWithResult":
        self.result = self._tests
        return self
    

    @property
    def _tests(self):
        try:
            return Test.objects.all()
        except Test.DoesNotExist:
            return None
    


