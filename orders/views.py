from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .forms import CheckoutForm, ShippingAddressForm
from django.shortcuts import redirect
from .models import Order, Citys, ShippingAddress, OrderProduct
from dal import autocomplete
from django.contrib.auth import get_user_model
import requests


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Citys.objects.all()
        print(qs)
        '''
        department = self.forwarded.get('department', None)
        if self.department:
            qs = qs.filter(department=department)
        '''
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ShippingView(LoginRequiredMixin, FormView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'checkout.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = self.form_class
        order = Order.objects.get(user=self.request.user, ordered=False)

        context = {
            'form': form,
            'order': order,

        }
        return render(request, self.template_name, context)


class CheckoutView(LoginRequiredMixin, FormView):

    model = Order
    template_name = 'checkout.html'
    form_class = CheckoutForm
    form_address = ShippingAddressForm

    def post(self, request):
        form = self.form_class(request.POST)
        form_2 = self.form_address(request.POST)

        print(form_2.errors)
        print('-----------')
        print(form.errors)
        if(not form.cleaned_data['use_default_shipping_address']):
            if(form.is_valid() and form_2.is_valid()):

                order_qs = Order.objects.filter(
                    user=request.user, ordered=False)
                if order_qs.exists():
                    order = order_qs[0]

                    instance_form2 = form_2.save(commit=False)
                    instance_form2.user = get_user_model().objects.get(username=request.user.username)
                    instance_form2.save()
                    shipping_new = ShippingAddress.objects.filter(
                        user=request.user, is_default=False)
                    if(shipping_new.exists()):
                        shipping = shipping_new[0]
                        order.shipping_address = shipping
                        order.use_default_shipping_address = False
                        order.payment_method = form.cleaned_data['payment_method']
                        order.ordered = True

                        order.save()
                        orders_products = OrderProduct.objects.filter(
                            user=request.user,
                            ordered=False
                        ).update(ordered=True)
                        if(form.cleaned_data['payment_method'] == 'Credit Card'):
                            r = requests.post(url='https://payment-restapi.herokuapp.com/payment-service', json={
                                'monto': order.get_total,
                                'credit_card': form.cleaned_data['credit_card'],
                                'username': order.user.username,
                                'correo': order.user.email,
                                'tienda': 'motiek-shop',

                            })
                            

                return redirect('home')
        else:
            try:
                shipping_qs = ShippingAddress.objects.filter(
                    user=request.user, is_default=True)
                order_qs = Order.objects.filter(
                    user=request.user, ordered=False)
                if order_qs.exists():
                    order = order_qs[0]
                    if(shipping_qs.exists()):
                        shipping = shipping_qs[0]
                        order.shipping_address = shipping
                        order.use_default_shipping_address = True
                        order.payment_method = form.cleaned_data['payment_method']
                        order.ordered = True

                        order.save()
                        orders_products = OrderProduct.objects.filter(
                            user=request.user,
                            ordered=False
                        ).update(ordered=True)

                    return redirect('home')
            except:
                return redirect('home')

        order = Order.objects.get(user=self.request.user, ordered=False)
        return render(request, self.template_name, {
            'form': form,
            'order': order,
            'form_address': form_2

        })

    def get(self, request):
        form = self.form_class
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'form': form,
                'order': order,
                'form_address': self.form_address
            }
            return render(request, self.template_name, context)
        except:
            return render(request, 'cart.html')
