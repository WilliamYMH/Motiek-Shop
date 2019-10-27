from django import template
from ..models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].products.count()
    return 0


@register.filter
def attrs_citys(value):
    return value.as_widget(attrs={
        'class': 'dropdown_item_select checkout_input',
        'id': 'checkout_city'
    })

@register.filter
def attrs_payments(value):
    return value.as_widget(attrs={
        'class': 'dropdown_item_select checkout_input_payment',
        'id': 'checkout_city',
        'onChange': "creditCard(this.value)",
    })

@register.filter
def attrs_inputs_address(value):
    return value.as_widget(attrs={
        'class': 'checkout_input',
        'id': 'checkout_address'
    })
