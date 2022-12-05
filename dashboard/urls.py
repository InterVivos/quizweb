from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#Definir nombre de la aplicación
app_name = 'dashboard'

#Importar urls de las páginas de la aplicación con sus vistas
urlpatterns = [
    #path('dashboard', views.MainView.as_view(), name = "home"),
    #path('dashboard', login_required(function=TemplateView.as_view(template_name="dashboard/index.html"), login_url='/login'), name="home"),
    path('dashboardindex', login_required(function=views.MainView1.as_view(), login_url='/login'), name="home1"),
    path('dashboard', login_required(function=views.MainView.as_view(), login_url='/login'), name="home"),
    path('save-quiz', views.saveQuiz, name="save-quiz"),
    path('quiz/send-quiz', views.sendQuiz, name="send-quiz"),
    path('quiz/<slug:slug>', views.CodigoQuiz.as_view(), name = 'quiz'),
    #path('edit-quiz/<slug:slug>', views.EditarQuiz.as_view(), name = 'edit-quiz'),
    path('edit-quiz', views.editarQuizFunc, name = 'edit-quiz'),
]

###Prueba de páginas
import os
#archivos = os.scandir(os.getcwd() + "/dashboard/templates/dashboard")
with os.scandir(os.getcwd() + "/dashboard/templates/dashboard") as archivos:
    for archivo in archivos:
        if not archivo.name.startswith('.'):
            #archivoN = "dashboard/" + archivo.name
            #if archivo.name == 'index.html': archivo.name = "dashboard.html"
            if archivo.name == "index.html" or archivo.name == "edit-quiz.html": continue
            archivoN = archivo.name
            #urlpatterns.append(path(archivoN, TemplateView.as_view(template_name="dashboard/" + archivo.name), name=archivo.name))
            urlpatterns.append(path(archivoN, login_required(function=TemplateView.as_view(template_name="dashboard/" + archivo.name), login_url='/login'), name=archivo.name))