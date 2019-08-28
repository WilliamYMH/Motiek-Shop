from django.shortcuts import render, HttpResponseRedirect, redirect, render
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.urls import reverse_lazy


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('/')
        self.object = None
        return super().get(request, *args, **kwargs)


class LoginUser(FormView):

    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def post(self, request):
        if(request.POST.get('type_f', None) == 'login'):
            return LoginView.as_view()(self.request)
        elif(request.POST.get('type_f', None) == 'reset_password'):
            return PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html')(self.request)
