# Generated by Django 5.0.6 on 2024-07-19 02:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0009_alter_estimates_estimate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimates',
            name='estimate_date',
            field=models.DateField(default=datetime.date(2024, 7, 19)),
        ),
    ]
