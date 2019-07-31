from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, redirect
from .models import Product
# Create your views here.


class ProductList(ListView):
    model = Product
