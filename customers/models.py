from django.db import models 
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from phone_field import PhoneField
from gst_field.formfields import GSTField
from cryptography.fernet import Fernet

# Create your models here.
class Customer(models.Model):
    class CustomerType(models.TextChoices):
        INDIVIDUAL = "INDIVIDUAL", _("Individual")
        ORGANIZATION = "ORGANIZATION", _("Organization")
    class CustomerStatus(models.TextChoices):
        ACTIVE = "ACTIVE", _("Active")
        INACTIVE = "INACTIVE", _("Inactive")
    class GstTreatment(models.TextChoices):
        REGISTERED = "REGISTERED", _("Registered")
        UNREGISTERED = "UNREGISTERED", _("Unregistered")
    
    class PaymentTermsChoices(models.TextChoices):
        DUE_ON_RECEIPT = "DUE_ON_RECEIPT", _("Due_on_receipt")
        DUE_AFTER_ONE_WEEK = "DUE_AFTER_ONE_WEEK", _("Due_after_one_week")
        DUE_AFTER_ONE_MONTH = "DUE_AFTER_ONE_MONTH", _("Due_after_one_month")

    type = models.CharField(max_length=16, choices=CustomerType, default=CustomerType.INDIVIDUAL)
    display_name = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=60)
    organization_name = models.CharField(max_length=100, unique=True)
    mobile_number = PhoneField(unique=True, help_text='Contact phone number')
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.TextField(blank=True)
    status = models.CharField(choices=CustomerStatus, default=CustomerStatus.ACTIVE)
    receivables = models.IntegerField(default=0, blank=True)
    gst_treatment = models.CharField(choices=GstTreatment, default=GstTreatment.UNREGISTERED)
    gstin = GSTField()
    _aadhar_number = models.CharField(max_length=255, db_column='aadhar_number', unique=True)
    payment_terms = models.CharField(choices=PaymentTermsChoices, default=PaymentTermsChoices.DUE_ON_RECEIPT)
    upi_number = models.CharField(unique=True, blank=True, max_length=50, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.display_name

