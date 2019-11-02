from django import forms
from .models import Order, ShippingAddress

PAYMENT_METHODS_CHOICES =(
    ('Paypal', 'Paypal'),
    ('Credit Card', 'Credit Card'),
    ('Payu', 'Payu')
)

class CheckoutForm(forms.ModelForm):

    payment_method = forms.ChoiceField(choices = PAYMENT_METHODS_CHOICES, required=True)
    class Meta:
        model = Order
        fields = ('payment_method', 'coupon', 'shipping_address',
                  'use_default_shipping_address')


class ShippingAddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ('address', 'city', 'codigo_postal', 'number_telephone')
        # widgets = {
       #     'city': autocomplete.ModelSelect2(url='city-autocomplete')
       # }
