from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import accInfo
from django.contrib.auth.models import User


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']