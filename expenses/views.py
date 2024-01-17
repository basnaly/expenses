from django.shortcuts import render
from .models import User, Currency, CreditCard, DebitCard, Cash, Payment
from django.contrib.auth import authenticate, login, logout
from expenses.forms import RegisterForm, LoginForm, CurrencyForm, CreditCardForm, DebitCardForm, CashForm, ProfileForm, PaymentForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from datetime import datetime
import calendar


def index(request):
    # get payments for current month
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        today = datetime.today()
        current_month = today.month # "1"
        current_year = today.year # "2024"
        selected_date = today
        user_payments = Payment.objects.filter(owner=user, payment_date__month=current_month, payment_date__year=current_year)
        
        # curent_list_payments = []
        # for el in user_payments:
        #     if el.credit_card not in curent_list_payments:
        #         curent_list_payments.append(el.credit_card)
        #     if el.cash not in curent_list_payments:
        #         curent_list_payments.append(el.cash)
        #     if el.debit_card not in curent_list_payments:
        #         curent_list_payments.append(el.debit_card)  
            
        # for el in curent_list_payments:
        #     if isinstance(el, CreditCard):
        #         print(el)
        #         print("----")
        #         list_paiments_by_card_el = [el1 for el1 in user_payments if el1.credit_card.id == el.id and el1.credit_card_amount]
        #         print(list_paiments_by_card_el)
        

        # get payments for selected month
        selected_month = request.GET.get("month")
        selected_year = request.GET.get("year")
        user_selected_payments = []
    
        # if user selected month and year
        if selected_month and selected_year:
            selected_date = datetime.strptime(f"01-{selected_month}-{selected_year}", "%d-%m-%Y") # "2023-02-01 00:00:00"
            selected_month = int(selected_month) # 1
            user_selected_payments = Payment.objects.filter(owner=user, payment_date__month=selected_month, payment_date__year=selected_year)
        
        return render(request, "expenses/index.html", {
            "payments": user_payments,
            "selected_payments": user_selected_payments,
            "current_month": calendar.month_name[current_month], # "January"
            "current_year": current_year, # "2024"
            "selected_month": calendar.month_name[selected_month or current_month], # "December"
            "selected_year": selected_year, # "2023"
            "selected_month_year": selected_date or None,
            "current_month_year": today # "2024-01-09 15:22:00"  
        })
    else:
        return render(request, "expenses/index.html", {})
    
    
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
def profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        return render(request, "expenses/profile.html", {
            "form": ProfileForm(initial={
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            })
        })
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            current_password = form.cleaned_data.get("current_password")
            new_password = form.cleaned_data.get("new_password")
            confirmation = form.cleaned_data.get("confirmation")
            
            if not check_password(current_password, user.password):
                messages.error(request, "The current password doesn't match.")
                return render(request, "expenses/profile.html", {
                    "form": form
                })
                
            if new_password:
                if new_password != confirmation:
                    messages.error(request, "The new password does't match confirmation.")
                    return render(request, "expenses/profile.html", {
                        "form": form
                    })
                else:
                    user.set_password(new_password)
                    
            try: 
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                update_session_auth_hash(request, user)
            except IntegrityError:
                messages.error(request, "Something went wrong. Try again later.")
                return render(request, "expenses/profile.html", {
                    "form": form
                })
            messages.success(request, f"Your profile was successfully updated!")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "The form is not valid!")
            return render(request, "expenses/profile.html", {
                    "form": form
                })
                

@login_required
def add_payment_method(request):
    user = User.objects.get(id=request.user.id) 
    user_credit_cards = CreditCard.objects.filter(owner=user)
    user_debit_cards = DebitCard.objects.filter(owner=user)
    user_cash_items = Cash.objects.filter(owner=user)
    
    user_currencies = Currency.objects.filter(owner=user).values('currency_name', 'id')
    currency_options = [(el['id'], el['currency_name']) for el in user_currencies]
    
    if request.method == "GET":
        debit_card_form = DebitCardForm()
        cash_form = CashForm()
        debit_card_form.fields['currency'].widget.choices = currency_options
        cash_form.fields['currency'].widget.choices = currency_options
        
        return render(request, "expenses/add_payment_method.html", {
            "credit_card_form": CreditCardForm,
            "debit_card_form": debit_card_form,
            "cash_form": cash_form,
            "credit_cards": user_credit_cards,
            "debit_cards": user_debit_cards,
            "cash_items": user_cash_items,
        })
        
        
@login_required
def create_currency(request):
    user = User.objects.get(id=request.user.id)
    user_currencies = Currency.objects.filter(owner=user)
    
    if request.method == "GET":
        return render(request, "expenses/create_currency.html", {
            "form": CurrencyForm(),
            "currencies": user_currencies
        })
        
    else:
        form = CurrencyForm(request.POST) 
        if form.is_valid():
            currency_name = form.cleaned_data.get("currency_name")
            try:
                new_currency = Currency.objects.create(
                    currency_name = currency_name,
                    owner = user
                )
                new_currency.save()
            except IntegrityError:
                messages.error(request, "Something went wrong. Try again later.")
                return render(request, "expenses/create_currency.html", {
                    "form": form,
                    "currencies": user_currencies
                })
            messages.success(request, f"Your { currency_name } currency was successfully created!")
            return HttpResponseRedirect(reverse("create_currency"))
        else:
            messages.error(request, "The form is not valid!")
            return render(request, "expenses/create_currency.html", {
                "form": form,
                "currencies": user_currencies
            })


@csrf_exempt
@login_required
def edit_currency(request, name):
    user = User.objects.get(id=request.user.id)
    user_currency = Currency.objects.get(owner=user, id=name)
    data = json.loads(request.body)
    changed_currency_name = data.get("changed_currency_name")
    if not changed_currency_name:
        return JsonResponse({
            "message": "The input field cannot be empty!"
        })
    try:
        user_currency.currency_name = changed_currency_name
        user_currency.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"Your { user_currency.currency_name } currency was successfully updated!"
    })


@csrf_exempt
@ login_required
def delete_currency(request, name):
    user = User.objects.get(id=request.user.id)
    try:
        currency = Currency.objects.get(owner=user, id=name)
    except Currency.DoesNotExist:
        return JsonResponse({
            "message": "It is not your currency!"
        })
    
    if request.method == "DELETE":
        try:
            currency.delete()
        except IntegrityError:
            return JsonResponse({
                "message": "Something went wrong. Try again later."
            })
        return JsonResponse({
            "message": f"Your { currency.currency_name } currency was successfully deleted!"
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
            messages.success(request, f"Your { card_name } credit card was successfully created!")
            return HttpResponseRedirect(reverse("add_payment_method"))
        else:
            messages.error(request, "The form is not valid!")
            return HttpResponseRedirect(reverse("add_payment_method"))
              

@csrf_exempt    
@login_required
def edit_credit_card(request, name):
    user = User.objects.get(id=request.user.id)
    user_credit_card = CreditCard.objects.get(owner=user, id=name)
    data = json.loads(request.body)
    changed_card_name = data.get('changed_card_name')
    changed_expiried_date = data.get('changed_expiried_date')
    if not changed_card_name or not changed_expiried_date:
        return JsonResponse({
            "message": "The input fields cannot be empty!"
        })
    try:
        user_credit_card.card_name = changed_card_name
        user_credit_card.expiried_date = changed_expiried_date
        user_credit_card.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"Your { user_credit_card.card_name } credit card was successfully updated!"
    })


@csrf_exempt       
@login_required
def delete_credit_card(request, name):
    user = User.objects.get(id=request.user.id)
    try:
        credit_card = CreditCard.objects.get(owner=user, id=name)
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

             
@login_required
def create_debit_card(request):
    user = User.objects.get(id=request.user.id)  
    
    if request.method == "POST":
        debit_card_form = DebitCardForm(request.POST)
        if debit_card_form.is_valid():
            card_name = debit_card_form.cleaned_data.get("card_name")
            currency = debit_card_form.cleaned_data.get("currency")
            reminder = debit_card_form.cleaned_data.get("reminder")
            note = debit_card_form.cleaned_data.get("note")
            
            user_currency = Currency.objects.get(owner=user, id=currency)
            
            try:
                new_debit_card = DebitCard.objects.create(
                    card_name = card_name,
                    currency = user_currency,
                    reminder = reminder,
                    note = note,
                    owner = user
                )
                new_debit_card.save()
            except IntegrityError:
                messages.error(request,  "Something went wrong. Try again later.")
                return HttpResponseRedirect(reverse("add_payment_method"))
            messages.success(request, f"Your { card_name } debit card was successfully created!")
            return HttpResponseRedirect(reverse("add_payment_method"))
        else:
            messages.error(request, "The form is not valid!")
            return HttpResponseRedirect(reverse("add_payment_method"))
        
        
@csrf_exempt
@login_required
def edit_debit_card(request, name):
    user = User.objects.get(id=request.user.id)
    user_debit_card = DebitCard.objects.get(owner=user, id=name)
    
    data = json.loads(request.body)
    changed_card_name = data.get("changed_card_name")
    changed_currency = data.get("changed_currency")
    changed_reminder = data.get("changed_reminder")
    changed_note = data.get("changed_note")
    if not changed_card_name or not changed_currency or not changed_reminder:
        return JsonResponse({
            "message": "The input fields cannot be empty!"
        })
    try:
        user_debit_card.card_name = changed_card_name
        user_debit_card.currency = changed_currency
        user_debit_card.reminder = changed_reminder
        user_debit_card.note = changed_note
        user_debit_card.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"Your { user_debit_card.card_name } debit card was successfully updated!"
    })


@csrf_exempt
@login_required
def add_money_debit_card(request, name):
    user = User.objects.get(id=request.user.id)
    user_debit_card = DebitCard.objects.get(owner=user, id=name)
    data = json.loads(request.body)
    add_money = data.get("add_money")
    if not add_money:
        return JsonResponse({
            "message": "The input cannot be empty!"
        })
    try:
        user_debit_card.reminder = user_debit_card.reminder + int(add_money)
        user_debit_card.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"The reminder on your {user_debit_card.card_name} debit card was successfully updated!"
    })
    
    
@csrf_exempt
@login_required
def delete_debit_card(request, name):
    user = User(id=request.user.id)      
    try:
        debit_card = DebitCard.objects.get(owner=user, id=name)
    except DebitCard.DoesNotExist:
        return JsonResponse({
            "message": "It is not your credit card!"
        })
    if request.method == "DELETE":
        try:
            debit_card.delete()
        except IntegrityError:
            return JsonResponse({
                "message": "Something went wrong. Try again later."
            })
    return JsonResponse({
        "message": f"Your { debit_card } debit card was succesfully deleted!"
    })
    
    

@login_required
def create_cash(request):
    user = User.objects.get(id=request.user.id) 
    user_cash_items = Cash.objects.filter(owner=user)
    if request.method == "POST":    
        cash_form = CashForm(request.POST)
       
        if cash_form.is_valid():
            currency = cash_form.cleaned_data.get("currency")
            reminder = cash_form.cleaned_data.get("reminder")
            
            user_currency = Currency.objects.get(owner=user, id=currency)
            try:
                new_cash = Cash.objects.create(
                    currency = user_currency,
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
        user_cash.reminder = user_cash.reminder + float(add_cash)
        user_cash.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"Your {user_cash.currency} cash was successfully updated!"
    })
    
    
@csrf_exempt  
@login_required
def edit_cash(request, name):
    user = User.objects.get(id=request.user.id)
    user_cash = Cash.objects.get(owner=user, id=name)
    data = json.loads(request.body)
    changed_cash_currency = data.get("changed_cash_currency")
    changed_cash_reminder = data.get("changed_cash_reminder")
    if not changed_cash_currency or not changed_cash_reminder:
        return JsonResponse({
            "message": "The input fields cannot be empty!"
        })
    
    try:
        user_cash.currency = changed_cash_currency
        user_cash.reminder = changed_cash_reminder
        user_cash.save()
    except IntegrityError:
        return JsonResponse({
            "message": "Something went wrong. Try again later."
        })
    return JsonResponse({
        "message": f"Your {user_cash.currency} cash was successfully updated!"
    })    
    

@csrf_exempt
@login_required
def delete_cash(request, name):
    user = User.objects.get(id=request.user.id)   
    try:
        cash = Cash.objects.get(owner=user, id=name)
    except Cash.DoesNotExist:
        return JsonResponse({
            "message": "It is not your cash!"
        })    
        
    if request.method == "DELETE":
        try:
            cash.delete()
        except IntegrityError:
            return JsonResponse({
                "message": "Something went wrong. Try again later."
            })
    return JsonResponse({
        "message": f"Your {cash.currency} cash was successfully deleted!"
    })
    
   
@login_required
def create_payment(request):
    user = User.objects.get(id=request.user.id)
    user_payments = Payment.objects.filter(owner=user)
    
    user_credit_cards = CreditCard.objects.filter(owner=user).values('card_name', 'id')
    credit_card_options = [(el['id'], el['card_name']) for el in user_credit_cards]
    
    user_cash = Cash.objects.filter(owner=user).values('currency', 'id')
    cash_options = [(el['id'], el['currency']) for el in user_cash]
    
    user_debit_cards = DebitCard.objects.filter(owner=user).values('card_name', 'id')
    debit_card_options = [(el['id'], el['card_name']) for el in user_debit_cards]
    
    if request.method == 'GET':
        form = PaymentForm()
        form.fields['credit_card'].widget.choices = credit_card_options
        form.fields['cash'].widget.choices = cash_options
        form.fields['debit_card'].widget.choices = debit_card_options
        return render(request, "expenses/payment.html", {
            "form": form,
            "payments": user_payments
        })
        
    else:
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_date = form.cleaned_data.get("payment_date")
            place = form.cleaned_data.get("place")
            purchase_type = form.cleaned_data.get("purchase_type")
            credit_card = form.cleaned_data.get("credit_card")
            credit_card_amount = form.cleaned_data.get("credit_card_amount")
            cash = form.cleaned_data.get("cash")
            cash_amount = form.cleaned_data.get("cash_amount")
            note = form.cleaned_data.get("note")
            debit_card = form.cleaned_data.get("debit_card")
            debit_card_amount = form.cleaned_data.get("debit_card_amount")
            
            # get object of CreditCard or Cash by id (foreign key)
            user_credit_card = CreditCard.objects.get(owner=user, id=credit_card)
            user_debit_card = DebitCard.objects.get(owner=user, id=debit_card)
            user_cash = Cash.objects.get(owner=user, id=cash)
            try:
                new_payment = Payment.objects.create(
                    payment_date = payment_date,
                    place = place,
                    purchase_type = purchase_type,
                    credit_card = user_credit_card,
                    credit_card_amount = credit_card_amount,
                    cash = user_cash,
                    cash_amount = cash_amount,
                    note = note,
                    debit_card = user_debit_card,
                    debit_card_amount = debit_card_amount,
                    owner = user
                )
                new_payment.save()
                if debit_card_amount:
                    user_debit_card.reminder = int(user_debit_card.reminder) - int(debit_card_amount)
                    user_debit_card.save()
                    print(user_debit_card.reminder)
            except IntegrityError as e:
                print(e)
                messages.error(request, "Something went wrong. Try again later.")
                return render(request, "expenses/payment.html", {
                    "form": form,
                    "payments": user_payments
                })
            messages.success(request, f"Your payment for {purchase_type} was successfully created")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "The form is not valid!")
            return render(request, "expenses/payment.html", {
                "form": form,
                "payments": user_payments
            })