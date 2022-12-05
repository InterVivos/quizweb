from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'autor', 'titulo')
    readonly_fields = ('slug',)