from orders.models import OrderProduct, Order
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Product

# Create your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 2


class ProductDetail(DetailView):
    model = Product


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "This product quantity was updated.")
            return redirect("home")
        else:
            order.products.add(order_product)
            messages.info(request, "This product was added to your cart.")
            return redirect("home")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
        return redirect("home")
