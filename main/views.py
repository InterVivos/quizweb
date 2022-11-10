from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("success", content_type='text/plain')
                #return redirect('main:home')
            else:
                return HttpResponse("error", content_type='text/plain')
                #messages.error(request, "Usuario o contraseña incorrecta")
        context = {}
        return render(request, "main/login.html", context)

def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return HttpResponse("success", content_type='text/plain')
                #messages.success(request, "Cuenta creada")
            else:
                messages = ""
                for v in form.error_messages.values():
                    messages += v +'\n'
                return HttpResponse(messages, content_type='text/plain')
        context = {'form':form}
        return render(request, "main/signup.html", context)

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context