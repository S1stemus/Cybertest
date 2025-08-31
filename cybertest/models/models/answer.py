from django.db import models


class Answer(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name="Название",
        null = False,
        blank = False
    )
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Вопрос",
        related_name="questions",
        related_query_name="question",
    )
    choices = models.IntegerField(
        default = 0,
        blank = False,
        null = False,
    )
    class Meta :
        app_label = "models"
        db_table = "answers"
        verbose_name_plural = "Ответы"
        verbose_name = "Ответ"


