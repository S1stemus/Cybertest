from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome
from api.services.user.create import CreateUserService
from api.serializers.user.register import UserRegisterSerializer
from api.serializers.user.show import UserSerializer
from api.services.user.update import UserUpdateService
from api.services.user.show import UserShowService
from rest_framework.permissions import AllowAny, IsAuthenticated



class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Пользователи"],
        summary="Обновляет пользователя по id",
        description="Обновляет пользователя по id",
        responses={200: UserSerializer},
        request=UserSerializer,
    )
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            UserUpdateService,
            {"user_id": kwargs["id"], "current_user": request.user}
            | request.data
        )
        return Response(UserSerializer(outcome.result).data)
class UserShowView(APIView):
    
    permission_classes = [AllowAny]
    @extend_schema(
        tags=["Пользователи"],
        summary="Возвращает пользователя по id",
        description="Возвращает пользователя по id",
        responses={200: UserSerializer},
    )
    def get(self, request, *args, **kwargs):
        
        outcome = ServiceOutcome(
            UserShowService, {"user_id": kwargs["id"]} 
        )
        return Response(UserSerializer(outcome.result).data)
    
    




class RegisterUserView(APIView):
    @extend_schema(
        tags=["Пользователи"],
        summary="Создает пользователя ",
        description="Создает пользователя",
        responses={200: UserSerializer},
        request=UserRegisterSerializer,
    )
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            CreateUserService(), request.data
        )
        return outcome.result
