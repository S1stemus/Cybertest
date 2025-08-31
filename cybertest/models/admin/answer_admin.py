from django.contrib import admin
from models.models import Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('name', 'question', 'choices')
    list_display = ('id','name', 'question', 'choices')
