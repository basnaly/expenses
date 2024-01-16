# Generated by Django 4.2.6 on 2024-01-11 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_remove_debitcard_expiried_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='debit_card',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='debit_cards', to='expenses.debitcard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='debit_card_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]