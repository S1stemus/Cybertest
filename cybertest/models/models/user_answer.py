from django.db import models



class UserAnswer(models.Model):
    is_correct_choices = [(0, "Нет"), (1, "Да")]
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Пользователь",
        related_name="user_answers",
        related_query_name="user_answer",
    )
    answer = models.ForeignKey(
        "Answer",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Вариант ответа",
        related_name="user_answers",
        related_query_name="user_answer",
    )
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name = "Вопрос",
        related_name ="user_answers",
        related_query_name = "user_answer",
        default = None
    )
    test = models.ForeignKey(
        "Test",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Тест",
        related_name="user_answers",
        related_query_name="user_answer",
        default = 1
    )
    is_correct_answer = models.IntegerField(
        choices = is_correct_choices,
        default = 0,
        blank = False,
        null = False
    ) 


    class Meta:
        app_label = "models"
        db_table = "user_answers"
        unique_together = ("answer", "user")
        verbose_name_plural = "Ответы пользователя"
        verbose_name = "Ответ пользователя"
