from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import User, Url

# Create your views here.
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm

class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'

class UrlListView(ListView):
    model = Url
    context_object_name = 'urls'
    
    queryset = [{'short_url': 'b2xVn2', 'long_url': 'https://www.google.com'}]
    template_name = "urls_index.html"