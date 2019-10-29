from .views import CheckoutView, CityAutocomplete, ShippingView, ListOrdersView
from django.urls import path
urlpatterns = [
    path('checkout', CheckoutView.as_view(), name="checkout"),
    path('city-autocomplete', CityAutocomplete.as_view(), name="city-autocomplete"),
    path('list-orders', ListOrdersView.as_view(), name="list_orders"),

]
