# Generated by Django 5.0.6 on 2024-06-11 18:24

import django.core.validators
import phone_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('ORGANIZATION', 'Organization')], default='INDIVIDUAL', max_length=16)),
                ('display_name', models.CharField(max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=60)),
                ('organization_name', models.CharField(max_length=100, unique=True)),
                ('mobile_number', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE')),
                ('receivables', models.IntegerField(blank=True, default=0)),
                ('gst_treatment', models.CharField(choices=[('REGISTERED', 'Registered'), ('UNREGISTERED', 'Unregistered')], default='UNREGISTERED')),
                ('_aadhar_number', models.CharField(db_column='aadhar_number', max_length=255, unique=True)),
                ('payment_terms', models.CharField(choices=[('DUE_ON_RECEIPT', 'Due_on_receipt'), ('DUE_AFTER_ONE_WEEK', 'Due_after_one_week'), ('DUE_AFTER_ONE_MONTH', 'Due_after_one_month')], default='DUE_ON_RECEIPT')),
                ('upi_number', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
    ]
