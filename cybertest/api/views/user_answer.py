
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from api.services.user_answer.create import CreateUserAnswerService
from api.services.user_answer.update import UpdateUserAnswerService
from api.services.user_answer.delete import UserAnswerDeleteService
from api.services.user_answer.result import ResultService
from service_objects.services import ServiceOutcome
from api.serializers.user_answer.create import UserAnswerCreateSerializer
from api.serializers.user_answer.show import UserAnswerShowSerializer
from api.serializers.user_answer.update import UserAnswerUpdateSerializer

class UserAnswerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Ответы пользователя"],
        summary="Создает ответ пользователя",
        description="Создает ответ пользователя",
        responses={201: UserAnswerShowSerializer},
        request=UserAnswerCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CreateUserAnswerService(),{"current_user": request.user} | request.data)
        return Response(UserAnswerShowSerializer(outcome.result).data, status=status.HTTP_201_CREATED)
        
class UserAnswerRetrieveView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Ответы пользователя"],
        summary="Изменяет ответ пользователя",
        description="Изменяет ответ пользователя",
        responses={200: UserAnswerShowSerializer},
        request= UserAnswerUpdateSerializer,
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UpdateUserAnswerService(),{"user_answer_id": kwargs["user_answer_id"],"current_user": request.user} | request.data)
        return Response(UserAnswerShowSerializer(outcome.result).data, status=status.HTTP_200_OK)
    @extend_schema(
        tags=["Ответы пользователя"],
        summary="Удаляет ответ пользователя",
        description="Удаляет ответ пользователя",
        responses={200: UserAnswerShowSerializer},
    )
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserAnswerDeleteService(),{"user_answer_id": kwargs["user_answer_id"],"current_user": request.user} | request.data)
        return Response(UserAnswerShowSerializer(outcome.result).data, status=status.HTTP_204_NO_CONTENT)
