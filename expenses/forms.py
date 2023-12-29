from django import forms
from .models import User
from django.contrib.auth import password_validation


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
    
    
class CreditCardForm(forms.Form):
    card_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of card', 'class': 'form-control mb-3'}), label='')
    expiried_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Expired date', 'class': 'form-control'}), label='')
    

class CashForm(forms.Form):
    currency = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Currency', 'class': 'form-control mb-3'}), label='')
    reminder = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Reminder', 'class': 'form-control'}), label='')