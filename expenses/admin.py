from django.contrib import admin
from .models import User, CreditCard, DebitCard, Cash, Payment

# Register your models here.

admin.site.register(User)
admin.site.register(CreditCard)
admin.site.register(DebitCard)
admin.site.register(Cash)
admin.site.register(Payment)