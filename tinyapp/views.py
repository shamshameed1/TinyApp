from datetime import date
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, View
from .models import User, Url
from .forms import UserRegisterForm
import string
import random
from django.forms import TextInput, ModelForm
from django.http import HttpResponseRedirect


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

class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'http://'})
        }

class UrlDetailView(DetailView):
    model = Url
    template_name = 'url_detail.html'

class UrlRedirectView(View):
    def get(self, request, short_url):
        long = Url.objects.values_list('long_url', flat=True).get(short_url = short_url)
        return HttpResponseRedirect(long)

class UrlCreateView(CreateView):
    form_class = UrlModelForm
    success_url ='/urls/'
    template_name = 'urls_new.html'

    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x 

    def form_valid(self, form):
        user = User.objects.first()
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = date.today()
        return super().form_valid(form)