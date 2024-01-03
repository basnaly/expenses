from django.shortcuts import render
from .models import User, CreditCard, Cash
from django.contrib.auth import authenticate, login, logout
from expenses.forms import RegisterForm, LoginForm, CreditCardForm, CashForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError

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


@login_required
def add_payment_method(request):
    user = User.objects.get(id=request.user.id) 
    user_credit_cards = CreditCard.objects.filter(owner=user)
    user_cash_items = Cash.objects.filter(owner=user)
    if request.method == "GET":
        return render(request, "expenses/add_payment_method.html", {
            "credit_card_form": CreditCardForm,
            "cash_form": CashForm,
            "credit_cards": user_credit_cards,
            "cash_items": user_cash_items
        })
    
    
@login_required
def create_credit_card(request):
    user = User.objects.get(id=request.user.id) 
    user_credit_cards = CreditCard.objects.filter(owner=user)
    if request.method == "POST":
        credit_card_form = CreditCardForm(request.POST)
        if credit_card_form.is_valid():
            card_name = credit_card_form.cleaned_data.get("card_name")
            expiried_date = credit_card_form.cleaned_data.get("expiried_date")
            try:
                new_credit_card = CreditCard.objects.create(
                    card_name = card_name,
                    expiried_date = expiried_date,
                    owner = user
                )
                new_credit_card.save()
            except IntegrityError:
                messages.error(request, "Something went wrong. Try again later.")
                return HttpResponseRedirect(reverse("add_payment_method"))
            messages.success(request, f"Your { card_name } credit card was successfully added!")
            return HttpResponseRedirect(reverse("add_payment_method"))
        else:
            messages.error(request, "The form is not valid!")
            return HttpResponseRedirect(reverse("add_payment_method"))
                

@login_required
def create_cash(request):
    user = User.objects.get(id=request.user.id) 
    user_cash_items = Cash.objects.filter(owner=user)
    if request.method == "POST":    
        cash_form = CashForm(request.POST)
        if cash_form.is_valid():
            currency = cash_form.cleaned_data.get("currency")
            reminder = cash_form.cleaned_data.get("reminder")
            try:
                new_cash = Cash.objects.create(
                    currency = currency,
                    reminder = reminder,
                    owner = user
                )
                new_cash.save()
            except IntegrityError:
                messages.error(request, "Something went wrong. Try again later")
                return HttpResponseRedirect(reverse("add_payment_method"))
            messages.success(request, f"Your { currency } cash was succefully created!")
            return HttpResponseRedirect(reverse("add_payment_method"))
        else:
            messages.error(request, "The form is not valid!")
            return HttpResponseRedirect(reverse("add_payment_method"))
        
 
@csrf_exempt       
@login_required
def delete_credit_card(request, name):
    user = User(id=request.user.id)
    try:
        credit_card = CreditCard.objects.filter(owner=user, id=name)
    except CreditCard.DoesNotExist:
        return JsonResponse({
            "message": "It is not your credit card!"
        })
        
    if request.method == "DELETE":
        try:
            credit_card.delete()
        except IntegrityError:
            return JsonResponse({
                "message": "Something went wrong. Try again later."
            })
    return JsonResponse({
        "message": f"Your { credit_card } credit card was succesfully deleted!"
    })
    
    
@csrf_exempt
@login_required
def add_cash(request, name):
    user = User.objects.get(id=request.user.id)
    user_cash = Cash.objects.get(owner=user, id=name)
    data = json.loads(request.body)
    add_cash = data.get('add_cash')
    if not add_cash:
        return JsonResponse({
            "message": "The input cannot be empty!"
        })
    try:
        user_cash.reminder = user_cash.reminder + int(add_cash)
        user_cash.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"Your {user_cash.currency} cash was successfully updated!"
    })
        