"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tinyapp.views import UrlCreateView, UrlDetailView, UrlRedirectView, UrlDeleteView, UrlUpdateView, UserLoginView
from tinyapp.views import UrlListView
from tinyapp.views import UserRegistrationView
from tinyapp.views import SeeAdminsView
from django.contrib.auth.views import LogoutView, PasswordChangeView



urlpatterns = [
    path('', UrlListView.as_view(), name='user_list'),
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('urls/', UrlListView.as_view(), name='urls'),
    path('urls/new/', UrlCreateView.as_view(), name='urls_new'),
    path('urls/<pk>/', UrlDetailView.as_view(), name = 'urls_detail'),
     path('urls/u/<short_url>/', UrlRedirectView.as_view(), name ='urls_redirect'),
    path('urls/delete/<pk>/', UrlDeleteView.as_view(), name = 'urls_delete'),
    path('urls/edit/<pk>/', UrlUpdateView.as_view(), name = 'urls_edit'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', PasswordChangeView.as_view()),
    path('userlist/', SeeAdminsView.as_view(), name='users_list')
]
