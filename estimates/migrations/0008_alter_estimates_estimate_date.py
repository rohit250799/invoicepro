# Generated by Django 5.0.6 on 2024-07-14 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0007_estimates_total_estimate_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimates',
            name='estimate_date',
            field=models.DateField(default=datetime.date(2024, 7, 14)),
        ),
    ]