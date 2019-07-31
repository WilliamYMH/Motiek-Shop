from django.shortcuts import render, HttpResponseRedirect, redirect, render
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
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
    success_url = '/'

    def post(self, request):
        if(request.POST.get('type_f', None) == 'login'):
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            return redirect('/')
        elif(request.POST.get('type_f', None) == 'reset_password'):
            return PasswordResetView.as_view()(self.request)
            # return render(request, 'registration/login.html', {'reset': True})

    def get(self, request):
        if(request.user.is_authenticated):
            return redirect('/')
        else:
            return render(request, 'registration/login.html')
