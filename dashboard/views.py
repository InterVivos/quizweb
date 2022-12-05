import json
from multiprocessing import get_context
from traceback import print_exc, print_stack
from django.contrib import messages
from django.forms import ModelChoiceField
from django.shortcuts import render, redirect
from django.views import View, generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import *

# Create your views here.

@csrf_exempt
def saveQuiz(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            idQuiz = request.POST.get("id")
            titulo = request.POST.get("titulo")
            contenido = request.POST.get("contenido")
            
            if(idQuiz is None):
                quiz = QuizForm({'autor':request.user, 'titulo':titulo, 'contenido':contenido, 'activo':True})

                if quiz.is_valid():
                    quiz.save()
                    return HttpResponse("success", content_type='text/plain')
                else:
                    return HttpResponse("error", content_type='text/plain')
            else:
                try:
                    quiz_a_editar = Quiz.objects.get(slug=idQuiz)
                    if(quiz_a_editar.autor == request.user):
                        quiz_a_editar.titulo = titulo
                        quiz_a_editar.contenido = json.loads(contenido)
                        #quiz_a_editar.contenido = contenido.replace('\"', '"').strip('"')
                        quiz_a_editar.save()
                        return HttpResponse("success", content_type='text/plain')
                    else:
                        return HttpResponse("error", content_type='text/plain')
                except Exception:
                    return HttpResponse("error", content_type='text/plain')

def sendQuiz(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            idQuiz = request.POST.get("quiz")
            idQuiz = idQuiz[idQuiz.rfind("/")+1:]
            alias = request.POST.get("alias")
            respuestas = request.POST.get("respuestas")
            try:
                quiz_org = Quiz.objects.get(slug=idQuiz)
                quiz_enviado = RespuestaForm({'quiz':quiz_org, 'alias':alias, 'respuestas': respuestas, 'puntaje':100})
                if quiz_enviado.is_valid():
                    quiz_enviado.save()
                    return HttpResponse("success", content_type='text/plain')
                else:
                    return HttpResponse("error", content_type='text/plain')
            except Exception as e:
                return HttpResponse("error", content_type='text/plain')

def pages_views(request):
    if not request.user.is_authenticated:
        return redirect('main:login')
    else:
        context = {}
        render(request, request.path(), context)

class MainView1(LoginRequiredMixin, View):
    template_name = "dashboard/index.html"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def get(self, request):
        return render(request, template_name=self.template_name)

class MainView(LoginRequiredMixin, generic.ListView):
    template_name = "dashboard/index1.html"
    login_url = '/login'
    model = Quiz
    paginate_by: 10

    def get_queryset(self):
        return super().get_queryset().filter(autor=self.request.user)

    '''def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        #context["quices"] = Quiz.objects.filter(autor=self.request.user)
        #context["quices"] = Quiz.objects.all()
        self.context["quices"] = Quiz.objects.all()
        return self.context'''
    
    #def get(self, request):
    #    return render(request, template_name=self.template_name, context=self.context)

def editarQuizFunc(request):
    if request.user.is_authenticated:
        idQuiz = request.GET.get('id')
        if(idQuiz is not None):
            quiz_a_editar = Quiz.objects.get(slug=idQuiz)
            if(quiz_a_editar.autor == request.user):
                context = {'object': quiz_a_editar}
                return render(request, "dashboard/edit-quiz.html", context)

class CodigoQuiz(generic.DetailView):
    model = Quiz
    template_name = "dashboard/quiz.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context