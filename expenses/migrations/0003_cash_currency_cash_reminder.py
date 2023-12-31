# Generated by Django 4.2.6 on 2023-12-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_creditcard_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='currency',
            field=models.CharField(default='ILS', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cash',
            name='reminder',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]