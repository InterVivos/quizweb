from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def pages_views(request):
    if not request.user.is_authenticated:
        return redirect('main:login')
    else:
        context = {}
        render(request, request.path(), context)

class MainView(LoginRequiredMixin, View):
    template_name = "dashboard/index.html"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def get(self, request):
        return render(request, template_name=self.template_name)