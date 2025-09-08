from django import views
from api.views.user import UserShowView, RegisterUserView, UserUpdateView
from api.views.test import ListTestView, ResultView, RetreiveTestView, CreateTestView
from api.views.question import ListQuestionView
from api.views.question import CreateQuestionView
from api.views.question import RetreiveQuestionView
from api.views.answer import AnswerRetreiveView, AnswerListView, AnswerCreateView
from api.views.user_answer import UserAnswerCreateView, UserAnswerRetrieveView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
    path("register/", RegisterUserView.as_view()),
    path("users/<int:id>/", UserShowView.as_view()),
    path("users/update/<int:id>/", UserUpdateView.as_view()),
    path("test/", ListTestView.as_view()),
    path("tests/", CreateTestView.as_view()),
    path("test/<int:test_id>/", RetreiveTestView.as_view()),
    path("questions/<int:test_id>/", ListQuestionView.as_view()),
    path("questions/", CreateQuestionView.as_view()),
    path("question/<int:question_id>/", RetreiveQuestionView.as_view()),
    path("answers/<int:question_id>/", AnswerListView.as_view()),
    path("answers/", AnswerCreateView.as_view()),
    path("answer/<int:answer_id>/", AnswerRetreiveView.as_view()),
    path("user/answers/<int:user_answer_id>/", UserAnswerRetrieveView.as_view()),
    path("user/answers/", UserAnswerCreateView.as_view()),
    path("result/<int:test_id>/", ResultView.as_view()),
]