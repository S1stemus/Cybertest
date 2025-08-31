from django.db import models

class Question(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name="Название",
        null = False,
        blank = False
    )
    test = models.ForeignKey(
        "Test",
        on_delete = models.CASCADE,
        null = False,
        blank=False,
        verbose_name="Тест",
        related_name="tests",
        related_query_name="test",
    )
    
    



