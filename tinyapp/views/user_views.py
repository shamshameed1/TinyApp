from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from tinyapp.forms import UserRegisterForm


class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/login/'
    template_name = 'register.html'

    def form_valid(self, form):
        self.request.session['username'] = form.cleaned_data['username']
        return super().form_valid(form)

class UserLoginView(LoginView):
    #form_class = UserLoginForm
    success_url = '/urls'
    
    def form_valid(self, form):
        self.request.session['username'] = form.cleaned_data['username']
        LoginView.redirect_authenticated_user
        return super().form_valid(form)

    