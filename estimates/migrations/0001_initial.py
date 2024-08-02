# Generated by Django 5.0.6 on 2024-08-01 19:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0003_alter_customer__aadhar_number_and_more'),
        ('items', '0005_alter_item_available_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimates',
            fields=[
                ('estimate_id', models.AutoField(primary_key=True, serialize=False)),
                ('estimate_number', models.CharField(max_length=30, unique=True)),
                ('estimate_date', models.DateField(default=datetime.date(2024, 8, 2))),
                ('offer_expiry_date', models.DateField()),
                ('subject', models.TextField()),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('SENT', 'Sent'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('EXPIRED', 'Expired')], default='DRAFT')),
                ('customer_notes', models.TextField(blank=True)),
                ('tax_from_source_type', models.CharField(choices=[('TDS', 'Tds'), ('TCS', 'Tcs')], default='TCS')),
                ('applicable_tax_percentage', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('shipping_charges_applicable', models.BooleanField(default=False)),
                ('spipping_charges', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('discount_applicable', models.BooleanField(default=False)),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('terms_and_conditions', models.CharField()),
                ('upload_additional_files', models.FileField(blank=True, null=True, upload_to='')),
                ('total_estimate_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='EstimateItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offered_quantity_to_customer', models.PositiveIntegerField()),
                ('selling_price_proposed_to_customer', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='estimates.estimates')),
            ],
        ),
    ]
