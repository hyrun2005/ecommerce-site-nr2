from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.cart_summary, name='cart_summary'),
    path("add/", views.cart_add, name='cart_add'),
    path("delete/", views.cart_delete, name='cart_delete'),
    path("refresh/", views.cart_refresh, name='cart_refresh'),
]