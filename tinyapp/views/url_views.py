from datetime import date
from django.views.generic import CreateView, ListView, DetailView, View, DeleteView, UpdateView
from tinyapp.models import User, Url
import string, random
from django.forms import TextInput, ModelForm
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin


class UrlListView(LoginRequiredMixin, ListView):
    login_url='/login/'

    model = Url
    context_object_name = 'urls'
    
    template_name = "urls_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        
        return context
    def get_queryset(self):
        
        current_user = self.request.user.id
        
        if current_user == None:
            return None
        
        return Url.objects.filter(user_id=current_user) 
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
        key = short_url

        if key in self.request.session.keys():
            self.request.session[key] += 1
        else:
            self.request.session[key] = 1
        print(self.request.session[key])
        return HttpResponseRedirect(long)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        return context

class UrlDeleteView(DeleteView):
    model = Url
    success_url = '/urls'

class UrlUpdateView(UpdateView):
    model = Url
   #form_class = UrlModelForm
    fields = ['long_url']
    success_url = '/urls'
    template_name = 'url_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') 
                 
        cookie_id = str(context['url']) 
        
        if self.request.session.get(cookie_id) == None:
            context['total_visits'] = 0
        else:
            context['total_visits'] = self.request.session.get(cookie_id)
        
        return context 
        
        return context
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        logged_in_user = self.request.session.get('username')
        
        logged_in_user_id = None
        
        if logged_in_user:
            logged_in_user_id = User.objects.filter(username=logged_in_user)[0].id
        
        if(self.object.user_id != logged_in_user_id):
            return HttpResponseForbidden()
        
        return super().get(request, *args, **kwargs)

class UrlCreateView(LoginRequiredMixin, CreateView):
    login_url='/login/'
    form_class = UrlModelForm
    success_url ='/urls/'
    template_name = 'urls_new.html'

    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x 

    def form_valid(self, form):
        current_user_id = self.request.user.id
        user = User.objects.filter(pk = current_user_id).first()
        #user = User.objects.first()
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = date.today()
        return super().form_valid(form)

