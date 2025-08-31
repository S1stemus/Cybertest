from django.db import models



class UserAnswer(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Пользователь",
        related_name="users",
        related_query_name="user",
    )
    answer = models.ForeignKey(
        "Answer",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Пользователь",
        related_name="answers",
        related_query_name="answer",
    )
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Вопрос",
        related_name="questions_",
        related_query_name="question",
        default=None
    )
    is_correct = models.BooleanField(
        default = False,
        blank = False,
        null = False,
    )

    class Meta:
        app_label = "models"
        db_table = "user_answers"
        unique_together = ("answer", "user")
        verbose_name_plural = "Ответы пользователя"
        verbose_name = "Ответ пользователя"
