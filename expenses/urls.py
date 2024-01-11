from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    
    path("add_payment_method", views.add_payment_method, name="add_payment_method"),
    
    path("create_credit_card", views.create_credit_card, name="create_credit_card"),
    path("edit_credit_card/<str:name>", views.edit_credit_card, name="edit_credit_card"),
    path("delete_credit_card/<str:name>", views.delete_credit_card, name="delete_credit_card"),
    
    path("create_debit_card", views.create_debit_card, name="create_debit_card"),
    path("add_money_debit_card/<str:name>", views.add_money_debit_card, name="add_money_debit_card"),
    path("edit_debit_card/<str:name>", views.edit_debit_card, name="edit_debit_card"),
    path("delete_debit_card/<str:name>", views.delete_debit_card, name="delete_debit_card"),
    
    path("create_cash", views.create_cash, name="create_cash"),
    path("add_cash/<str:name>", views.add_cash, name="add_cash"),
    path("edit_cash/<str:name>", views.edit_cash, name="edit_cash"),
    path("delete_cash/<str:name>", views.delete_cash, name="delete_cash"),
    
    path("create_payment", views.create_payment, name="create_payment"),
]