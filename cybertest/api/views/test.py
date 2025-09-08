import re
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.services.test.create import TestCreateService
from api.services.test.list import TestListService
from api.serializers.test.show import TestShowSerializer
from api.serializers.test.create import TestCreateSerializer
from api.serializers.test.result import TestresultSerializer
from api.services.test.delete import TestDeleteService
from api.services.test.update import TestUpdateService
from rest_framework.response import Response
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from api.services.user_answer.result import ResultService

class ListTestView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        tags=["Тесты"],
        summary="Возвращает список тестов",
        description="Возвращает список тестов",
        responses={200: TestShowSerializer},
    )
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(TestListService(),request.data)
        return Response(TestShowSerializer(outcome.result, many=True).data)
class CreateTestView(APIView):    
        
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        tags=["Тесты"],
        summary="Создает тест",
        description="Создает тест",
        responses={200: TestShowSerializer},
        request=TestCreateSerializer,
            
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(TestCreateService(),{"current_user": request.user} | request.data)
        return Response(TestShowSerializer(outcome.result).data)
    

    

class RetreiveTestView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Тесты"],
        summary="Обновляет тест по id",
        description="Обновляет тест по id",
        request=TestCreateSerializer,
        responses={205: TestShowSerializer},
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(TestUpdateService(),{"test_id": kwargs["test_id"], "current_user": request.user} | request.data)
        return Response(TestShowSerializer(outcome.result).data, status=status.HTTP_205_RESET_CONTENT)

    @extend_schema(
        tags=["Тесты"],
        summary="Удаляет тест по id",
        description="Удаляет тест по id",
        responses={204: TestShowSerializer},
    )
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(TestDeleteService(),{"test_id": kwargs["test_id"], "current_user": request.user} | request.data)
        return Response(TestShowSerializer(outcome.result).data, status=status.HTTP_204_NO_CONTENT)    
    
class ResultView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Результаты"],
        summary="Возвращает результат теста пользователя",
        description="Возвращает результат теста пользователя",
        responses={200: TestresultSerializer},
    )
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ResultService(),{"test_id": kwargs["test_id"],"current_user": request.user} | request.data)
        return Response(TestresultSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)
    
    



