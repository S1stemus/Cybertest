from django.db import models

class Test(models.Model):
    user = models.ManyToManyField(
        "User",
        related_name="tests",
        related_query_name="test",
        null=False,
        blank=False,
        verbose_name="Пользователи",
        )
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
