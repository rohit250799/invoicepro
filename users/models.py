from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from argon2 import PasswordHasher

# Create your models here.

ph = PasswordHasher()
class UserProfileInfo(AbstractUser):

    #user = models.OneToOneField(AbstractUser)
    class Plan_options(models.TextChoices):
        FREE = "FREE", _('Free')
        SILVER = "SILVER", _("Silver")
        GOLD = "GOLD", _("Gold") 

    class Country_options(models.TextChoices):
        INDIA = "INDIA", _("India")
        USA = "USA", _("Usa")
        EU = "EU", _("EU")
    
    class Currency_options(models.TextChoices):
        INR = "INR", _("Inr")
        USD = "USD", _("Usd")
        EUR = "EUR", _("Eur")
    
    mobile = models.CharField(max_length=15)
    plan_type = models.CharField(max_length=30, choices=Plan_options, default=Plan_options.FREE)
    #hashed_password = ph.hash()
    user_country = models.CharField(max_length=30, choices=Country_options, default=Country_options.INDIA)
    user_currency = models.CharField(max_length=25, choices=Currency_options, default=Currency_options.INR)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=35)
    

