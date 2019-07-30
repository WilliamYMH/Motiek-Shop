from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, redirect
from .models import Product
# Create your views here.


class ProductList(ListView):
    model = Product


class CreateUser(CreateView):
    model = User
    fields = ('username', 'email', 'password')
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('/')
        self.object = None
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save(commit=False)
        self.object = User.objects._create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])
        self.object.save()
        return HttpResponseRedirect('/login/')
