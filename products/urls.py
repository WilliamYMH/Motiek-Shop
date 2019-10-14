from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('product/<slug>/', views.ProductDetail.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    #path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
]
