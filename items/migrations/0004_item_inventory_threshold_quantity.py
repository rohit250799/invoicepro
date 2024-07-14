# Generated by Django 5.0.6 on 2024-07-12 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_rename_selling_rate_item_marked_price_by_user_for_sale_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='inventory_threshold_quantity',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
