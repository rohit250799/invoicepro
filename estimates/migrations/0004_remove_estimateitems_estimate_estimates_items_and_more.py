# Generated by Django 5.0.6 on 2024-09-14 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0003_rename_spipping_charges_estimates_shipping_charges_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimateitems',
            name='estimate',
        ),
        migrations.AddField(
            model_name='estimates',
            name='items',
            field=models.ManyToManyField(to='estimates.estimateitems'),
        ),
        migrations.AlterField(
            model_name='estimates',
            name='estimate_date',
            field=models.DateField(default=datetime.date(2024, 9, 14)),
        ),
    ]