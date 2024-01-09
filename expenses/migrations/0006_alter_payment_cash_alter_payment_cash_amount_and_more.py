# Generated by Django 4.2.6 on 2024-01-07 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_rename_amount_payment_cash_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cash',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='cash_items', to='expenses.cash'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cash_amount',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='credit_card',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='credit_cards', to='expenses.creditcard'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='credit_card_amount',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='note',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]