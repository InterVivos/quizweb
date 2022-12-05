from django import forms
from .models import *

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['autor', 'titulo', 'contenido', 'activo']

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['quiz', 'alias', 'respuestas', 'puntaje']