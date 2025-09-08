
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.services.question.list_by_test_id import QuestionListByTestIdService
from api.serializers.question.list import QuestionListSerializer
from api.serializers.question.create import QuestionCreateSerializer
from api.serializers.question.update import QuestionUpdateSerializer
from api.serializers.question.show import QuestionShowSerializer
from rest_framework.response import Response
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from api.services.question.delete import QuestionDeleteService
from api.services.question.update import QuestionUpdateService
from api.services.question.create import CreateQuestionService
from api.services.question.show import QuestionShowService
from rest_framework import status

class ListQuestionView(APIView):
    @extend_schema(
        tags=["Вопросы"],
        summary="Возвращает список вопросов по id теста",
        description="Возвращает список вопросов по id теста",
        responses={200: QuestionListSerializer},
        request=QuestionListSerializer,
    )
    def get(self, request, *args, **kwargs):
        user = None if request.user.is_anonymous else request.user
        outcome = ServiceOutcome(QuestionListByTestIdService(),{"test_id": kwargs["test_id"], "current_user": user} | request.query_params.dict())
        return Response(QuestionListSerializer(outcome.result, many=True).data)

class CreateQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Вопросы"],
        summary="Создает вопрос по id теста",
        description="Создает вопрос по id теста",
        responses={200: QuestionListSerializer},
        request=QuestionCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CreateQuestionService(),{ "current_user": request.user} | request.data)
        return Response(QuestionListSerializer(outcome.result).data)
    
class RetreiveQuestionView(APIView):

    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Вопросы"],
        summary="Возвращает вопрос по id",
        description="Возвращает вопрос по id",
        responses={200: QuestionListSerializer},
    )
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(QuestionDeleteService(), {"question_id": kwargs["question_id"], "current_user": request.user})
        return Response(QuestionListSerializer(outcome.result).data, status=status.HTTP_204_NO_CONTENT)
    @extend_schema(
        tags=["Вопросы"],
        summary="Обновляет вопрос по id",
        description="Обновляет вопрос по id",
        responses={200: QuestionListSerializer},
        request=QuestionUpdateSerializer,
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(QuestionUpdateService(), {"question_id": kwargs["question_id"], "current_user": request.user} | request.data)
        return Response(QuestionListSerializer(outcome.result).data)
    
    permission_classes = [AllowAny]
    @extend_schema(
        tags=["Вопросы"],
        summary="Возвращает вопрос по id ",
        description="Возвращает вопрос по id ",
        responses={200: QuestionShowSerializer},
    )
    def get(self, request, *args, **kwargs):
        user = None if request.user.is_anonymous else request.user
        outcome = ServiceOutcome(QuestionShowService(),{"question_id": kwargs["question_id"], "current_user": user} | request.data)
        return Response(QuestionShowSerializer(outcome.result, many=True).data)


