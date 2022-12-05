import json
from traceback import print_exc, print_stack
from django.contrib import messages
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
            titulo = request.POST.get("titulo")
            contenido = request.POST.get("contenido")
            
            quiz = QuizForm({'autor':request.user, 'titulo':titulo, 'contenido':contenido, 'activo':True})

            if quiz.is_valid():
                quiz.save()
                return HttpResponse("success", content_type='text/plain')
            else:
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

class MainView(LoginRequiredMixin, View):
    template_name = "dashboard/index1.html"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def get(self, request):
        return render(request, template_name=self.template_name)

class CodigoQuiz(generic.DetailView):
    model = Quiz
    template_name = "dashboard/quiz.html"