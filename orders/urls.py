from .views import CheckoutView, CityAutocomplete, ShippingView
from django.urls import path
urlpatterns = [
    path('checkout', CheckoutView.as_view(), name="checkout"),
    path('city-autocomplete', CityAutocomplete.as_view(), name="city-autocomplete"),
]
