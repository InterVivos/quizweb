from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

#Definir nombre de la aplicación
app_name = 'main'

#Importar urls de las páginas de la aplicación con sus vistas
urlpatterns = [
    path('', views.IndexView.as_view(), name = "home"),
    path('login', views.loginUser, name="login"),
    path('register', views.register, name="register")
]