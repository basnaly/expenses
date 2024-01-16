from django import forms
from .models import User
from django.contrib.auth import password_validation
from datetime import date


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), label='', validators=[password_validation.validate_password])
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmation', 'class': 'form-control'}), label='', validators=[password_validation.validate_password])
    
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control mb-3'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), label='', validators=[password_validation.validate_password])
    
    
class CurrencyForm(forms.Form):
    currency_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of currency', 'class': 'form-control mb-3'}), label='')


class CreditCardForm(forms.Form):
    card_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of card', 'class': 'form-control mb-3'}), label='')
    expiried_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Expired date', 'type': 'date', 'class': 'form-control'}), label='')
    
    
class DebitCardForm(forms.Form):
    card_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of card', 'class': 'form-control mb-3'}), label='')
    currency = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Select the currency', 'class': 'form-control select-data mb-3'}, choices=[]), label='')
    reminder = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Reminder', 'class': 'form-control mb-3'}), label='')
    note = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Notes', 'rows': 2, 'cols': 20, 'class': 'form-control mb-3'}), required=False, label='')
    

class CashForm(forms.Form):
    currency = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Select the currency', 'class': 'form-control select-data mb-3'}, choices=[]), label='')
    reminder = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Reminder', 'class': 'form-control'}), label='')
    
    
class ProfileForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), label='')
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Current Password', 'class': 'form-control'}), label='', validators=[password_validation.validate_password])
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'class': 'form-control'}), label='',required=False, validators=[password_validation.validate_password])
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmtion', 'class': 'form-control'}), label='', required=False, validators=[password_validation.validate_password])
    

class PaymentForm(forms.Form):
    payment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': str(date.today()), 'class': 'form-control mb-3'}), label='')
    place = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Place of payment', 'class': 'form-control mb-3'}), label='')
    purchase_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type of purchase', 'class': 'form-control mb-3'}), label='')
    note = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Notes', 'rows': 2, 'class': 'form-control'}), required=False, label='')
    credit_card = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Select the credit card', 'class': 'form-control select-data mb-3'}, choices=[]), required=False, label='')
    credit_card_amount = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'The sum', 'class': 'form-control mb-3'}), required=False, label='')
    cash = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Select the type of cash', 'class': 'form-control select-data mb-3'}, choices=[]), required=False, label='')
    cash_amount = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'The sum', 'class': 'form-control mb-3'}), required=False, label='')
    debit_card = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Select the debit card', 'class': 'form-control select-data mb-3'}, choices=[]), required=False, label='')
    debit_card_amount = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'The sum', 'class': 'form-control mb-3'}), required=False, label='')