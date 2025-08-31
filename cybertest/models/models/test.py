from turtle import update
from venv import create
from django.db import models

class Test(models.Model):
    name = models.CharField(
        max_length = 127,
        verbose_name="Название",
        null=False,
        blank=False,
    )

    class Meta:
        app_label = "models"
        db_table = "test"
        verbose_name_plural = "Тесты"
        verbose_name = "Тест"
