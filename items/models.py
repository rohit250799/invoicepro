from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Item(models.Model):
    class ItemStatus(models.TextChoices):
        ACTIVE = "ACTIVE", _("Active")
        INACTIVE = "INACTIVE", _("Inactive")

    class AvailableUnits(models.TextChoices):
        PCS = "PCS", _("Pcs")
        KG = "KG", _("Kg")
        LTR = "LTR", _("Ltr")
        MTR = "MTR", _("Mtr")

    class ItemType(models.TextChoices):
        GOODS = "GOODS", _("Goods")
        SERVICES = "SERVICES", _("Services")
        

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=ItemStatus, default=ItemStatus.ACTIVE)
    item_type = models.CharField(choices=ItemType)
    description = models.TextField(blank=True)
    marked_price_by_user_for_sale = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(choices=AvailableUnits, default=AvailableUnits.PCS)
    taxes_applicable = models.BooleanField(default=False)
    tax_percentage_on_item = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    available_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def __str__(self):
        return self.name