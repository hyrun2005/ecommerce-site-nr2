from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]