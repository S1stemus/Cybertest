from django.contrib import admin
from models.models import Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('name', 'test')
    list_display = ('name', 'test')
    list_display_links = ('name', 'test')