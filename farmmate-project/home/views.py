from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.

# def home(request):
#     return render(request, 'home/home.html', {})

class HomePageView(TemplateView):
    template_name = 'home/home.html'
    extra_context = {'today': datetime.today()}

class LoginView(LoginView):
    template_name = 'home/login.html'
    
