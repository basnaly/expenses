# Generated by Django 4.2.6 on 2024-01-15 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0017_cash_currency_debitcard_currency_payment_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='name',
            new_name='currency_name',
        ),
    ]