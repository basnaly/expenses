from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    def __srt__(self):
        return f"{self.username}, {self.first_name}, {self.last_name}, {self.email}"
    

class CreditCard(models.Model):
    card_name = models.CharField(max_length=48)
    expiried_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credit_cards")
    
    def __str__(self):
        return f"{self.card_name}, {self.expiried_date}, {self.owner}"


class Cash(models.Model):
    currency = models.CharField(max_length=16)
    reminder = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="currencies")
    
    def __str__(self):
        return f"{self.currency}, {self.reminder}, {self.owner}"
    
    