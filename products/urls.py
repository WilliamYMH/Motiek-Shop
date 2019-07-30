from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('sign_up/', views.CreateUser.as_view(), name='sign_up')
]
