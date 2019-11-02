from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('product/<slug>/', views.ProductDetail.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',
         views.remove_from_cart, name='remove-from-cart'),
    path('remove-product-from-cart/<slug>/', views.remove_single_product_from_cart,
         name='remove-single-product-from-cart'),
    path('clean-cart', views.clean_all_cart, name='clean-all-cart'),
    path('cart', views.CartView.as_view(), name='cart'),
]
