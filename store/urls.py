from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('product/<int:pk>/', views.product_info, name='product_info'),
    path('categories/<str:foo>/', views.categories, name='categories'),
    path('cart/', include('cart.urls'))
]