from django.shortcuts import render, redirect
from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UserChangeForm)
from django.contrib.auth import authenticate, login
from . import forms as users_forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,
                  'users/home.html',
                  {"name": "Anirudh"})


def users_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("Username:", username, '\n'
                                         'Password:', password)
            user = authenticate(request,
                                username=username,
                                password=password)
            login(request, user)
            return redirect('users_home')
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def users_registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_login')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required(login_url='users_login')
def users_change(request):
    # form = UserChangeForm(instance=request.user)
    form = users_forms.UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        # form = UserChangeForm(request.POST,
        #                       instance=request.user)
        form = users_forms.UserUpdateForm(request.POST,
                                          instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('users_home')

    context = {
        'form': form
    }
    return render(request, 'users/users_change.html',
                  context)


def users_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/users_users.html',context)
