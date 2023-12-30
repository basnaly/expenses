from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    
    path("add_payment_method", views.add_payment_method, name="add_payment_method"),
    path("add_credit_card", views.add_credit_card, name="add_credit_card"),
]