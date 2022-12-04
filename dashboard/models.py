import random
import string
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'Quices'
        verbose_name = 'Quiz'
        ordering = ["-fecha"]
    
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=256)
    contenido = models.JSONField()
    activo = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            while(True):
                self.slug = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if(Quiz.objects.filter(slug=self.slug).first is None): break
        super(Quiz, self).save(*args, **kwargs)

class Respuesta:
    class Meta:
        verbose_name_plural = 'Respuestas'
        verbose_name = 'Respuesta'
        ordering = ["-fecha"]
    
    fecha = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    alias = models.CharField(max_length=256, null=True, blank=True)
    puntaje = models.IntegerField(default=0)
    respuestas = models.JSONField