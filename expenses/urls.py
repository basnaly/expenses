from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    
    path("add_payment_method", views.add_payment_method, name="add_payment_method"),
    path("create_credit_card", views.create_credit_card, name="create_credit_card"),
    path("create_cash", views.create_cash, name="create_cash"),
    
    path("delete_credit_card/<str:name>", views.delete_credit_card, name="delete_credit_card"),
    
]