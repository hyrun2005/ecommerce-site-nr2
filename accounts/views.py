from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from .forms import registerForm
from django.views.decorators.csrf import  csrf_exempt
from django.contrib import messages

# Create your views here.
@csrf_exempt
def registration(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly created')
            return redirect('login')

    context = {'form': form}
    return render(request, 'sign_up.html', context=context)
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Username or Password is incorrect')

    template = 'login.html'
    context ={}
    return render(request, template, context=context)
@csrf_exempt
def logoutUser(request):
    logout(request)
    return redirect('login')