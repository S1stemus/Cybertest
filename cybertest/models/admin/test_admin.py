from django.contrib import admin
from models.models import Test

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_display_links = ('name',)