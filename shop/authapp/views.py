from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from authapp.forms import LoginForm, RegisterForm
from django.views.generic import CreateView


class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('auth:login')
    template_name = 'authapp/register.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'authapp/login.html'


class Logout(LogoutView):
    success_url = reverse_lazy('auth:login')

