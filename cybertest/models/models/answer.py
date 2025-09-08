from django.db import models


class Answer(models.Model):
    is_correct_choices = [(0, "Нет"), (1, "Да")]
    name = models.CharField(
        max_length = 255,
        verbose_name="Название",
        null = False,
        blank = False
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Пользователь",
        related_name="answers",
        related_query_name="answer",
        default=None
    )
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Вопрос",
        related_name="answers",
        related_query_name="answer",
    )
    choices = models.IntegerField(
        default = 0,
        blank = False,
        null = False,
    )
    is_correct = models.IntegerField(
        choices = is_correct_choices,
        default = 0,
        blank = False,
        null = False
    ) 


    class Meta :
        app_label = "models"
        db_table = "answers"
        verbose_name_plural = "Ответы"
        verbose_name = "Ответ"


