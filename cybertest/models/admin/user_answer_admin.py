from django.contrib import admin
from models.models import UserAnswer

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    fields = ('answer', 'user', 'question', 'is_correct')
    list_display = ('id', 'answer', 'user', 'question', 'is_correct')
    list_display_links = ('id', 'answer', 'user')