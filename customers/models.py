from django.db import models
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
from gst_field.formfields import GSTField

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

    type = models.CharField(max_length=16, choices=CustomerType, default=CustomerType.INDIVIDUAL)
    display_name = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=60)
    organization_name = models.CharField(max_length=100, unique=True)
    mobile_number = PhoneField(unique=True, help_text='Contact phone number')
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    status = models.CharField(choices=CustomerStatus, default=CustomerStatus.ACTIVE)
    receivables = models.IntegerField(default=0, blank=True)
    gst_treatment = models.CharField(choices=GstTreatment, default=GstTreatment.UNREGISTERED)
    GSTIN = GSTField()
    



