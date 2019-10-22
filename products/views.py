from orders.models import OrderProduct, Order
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, View
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib import messages
from .models import Product

# Create your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 2


class ProductDetail(DetailView):
    model = Product


class CartView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
        except:
            return render(self.request, 'cart.html')
        context = {
            'object': order
        }
        return render(self.request, 'cart.html', context)


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
            return redirect("cart")
        else:
            order.products.add(order_product)
            messages.info(request, "This product was added to your cart.")
            return redirect("cart")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, "This product was added to your cart.")
        return redirect("cart")


@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_item = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.products.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)


@login_required
def remove_single_product_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_item = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]

            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.products.remove(order_item)
                order_item.delete()

            messages.info(request, "This item quantity was updated.")
            return redirect("cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart", slug=slug)


@login_required
def clean_all_cart(request):
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        # OrderProduct.objects.all().delete()
        order = order_qs[0]
        order.products.all().delete()
        # order.products.clear()
        return redirect("cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product")
