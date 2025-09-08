
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from api.services.answer.create import AnswerCreateService
from service_objects.services import ServiceOutcome
from api.serializers.answer.create import AnswerCreateSerializer
from api.serializers.answer.show import AnswerShowSerializer
from api.serializers.answer.update import AnswerUpdateSerializer
from api.services.answer.list import AnswerListService
from api.services.answer.delete import AnswerDeleteService
from api.services.answer.update import AnswerUpdateService
from rest_framework import status
from drf_spectacular.utils import extend_schema

class AnswerListView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        tags=["Ответы"],
        summary="Возвращает список ответов",
        description="Возвращает список ответов",
        responses={200: AnswerShowSerializer},
    )
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(AnswerListService(),{"question_id": kwargs["question_id"],"current_user": request.user} | request.data)
        return Response(AnswerShowSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)
class AnswerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Ответы"],
        summary="Создает ответ",
        description="Создает ответ",
        responses={200: AnswerShowSerializer},
        request=AnswerCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(AnswerCreateService(),{"current_user": request.user} | request.data)
        return Response(
            AnswerShowSerializer(outcome.result).data, status=status.HTTP_200_OK)
class AnswerRetreiveView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Ответы"],
        summary="Удаляет ответ по id",
        description="Удаляет ответ по id",
        responses={204: AnswerShowSerializer},
    )
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(AnswerDeleteService(),{"answer_id": kwargs["answer_id"], "current_user": request.user} | request.data)
        return Response(AnswerShowSerializer(outcome.result).data, status=status.HTTP_204_NO_CONTENT)
    @extend_schema(
        tags=["Ответы"],
        summary="Обновляет ответ по id",
        description="Обновляет ответ по id",
        responses={205: AnswerShowSerializer},
        request=AnswerUpdateSerializer,
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(AnswerUpdateService(),{"answer_id": kwargs["answer_id"], "current_user": request.user} | request.data)
        return Response(AnswerShowSerializer(outcome.result).data, status=status.HTTP_205_RESET_CONTENT)