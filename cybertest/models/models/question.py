from django.db import models

class Question(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name="Название",
        null = False,
        blank = False
    )
    user = models.ForeignKey(
        "User",
        on_delete = models.CASCADE,
        null = False,
        blank = False,
        verbose_name = "Пользователь",
        related_name = "questions",
        related_query_name = "question",
        default = None
    )
    test = models.ForeignKey(
        "Test",
        on_delete = models.CASCADE,
        null = False,
        blank=False,
        verbose_name="Тест",
        related_name="questions",
        related_query_name="question",
    )
    class Meta :
        app_label = "models"
        db_table = "question"
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"
    
    



