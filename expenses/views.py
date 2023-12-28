from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from expenses.forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

def index(request):
    return render(request, "expenses/index.html", {
        
    })
    
    
def register(request):
    if request.method == "GET":
        return render(request, "expenses/register.html", {
            "form": RegisterForm
        })
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            confirmation = form.cleaned_data.get("confirmation")
            
            existing_user_with_email = User.objects.filter(email=email)
            if len(existing_user_with_email) != 0:
                messages.error(request, "The email already exist!")
                return render(request, "expenses/register.html", {
                    "form": form
                })
            
            if password != confirmation:
                messages.error(request, "Password must much confirmation!")
                return render(request, "expenses/register.html", {
                    "form": form
                })
            
            try:
                new_user = User.objects.create_user(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password = password,
                )
                new_user.save()
            except IntegrityError:
                messages.error(request, "The username alredy exists!")
                return render(request, "expenses/register.html", {
                    "form": form
                })
                
            login(request, new_user)
            messages.success(request, f"The user { username } was successfully created!")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Some of the values are not valid!")
            return render(request, "expenses/register.html", {
                    "form": form
                })


def login_view(request):
    if request.method == "GET":
        return render(request, "expenses/login.html", {
            "form": LoginForm
        })
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                messages.error(request, "Invalid username or password")
                return render(request, "expenses/login.html", {
                    "form": form
                })
        else:
            messages.error(request, "The form is not valid!")
            return render(request, "expenses/login.html", {
                    "form": form
                })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))