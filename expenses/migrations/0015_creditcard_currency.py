# Generated by Django 4.2.6 on 2024-01-14 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0014_alter_cash_currency_alter_debitcard_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='credit_card_currencies', to='expenses.currency'),
        ),
    ]
