import datetime
from django.db import models, transaction
from django.db.models import Max
from customers.models import Customer
from django.utils.translation import gettext_lazy as _
from items.models import Item

# Create your models here.

class Estimates(models.Model):
    class StatusType(models.TextChoices):
        DRAFT = "DRAFT", _("Draft")
        SENT = "SENT", _("Sent")
        ACCEPTED = "ACCEPTED", ("Accepted")
        REJECTED = "REJECTED", ("Rejected")
        EXPIRED = "EXPIRED", ("Expired")

    class TaxTypeAsTdsOrTcs(models.TextChoices):
        TDS = "TDS", _("Tds")
        TCS = "TCS", _("Tcs")
    
    estimate_id = models.AutoField(primary_key=True)
    estimate_number = models.CharField(max_length=30, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    estimate_date = models.DateField(default=datetime.date.today())
    offer_expiry_date = models.DateField()
    items = models.ManyToManyField(Item, through='EstimateItems') #testing
    subject = models.TextField()
    status = models.CharField(choices=StatusType, default=StatusType.DRAFT)
    customer_notes = models.TextField(blank=True)
    tax_from_source_type = models.CharField(choices=TaxTypeAsTdsOrTcs, default=TaxTypeAsTdsOrTcs.TCS)
    applicable_tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    shipping_charges_applicable = models.BooleanField(default=False)
    shipping_charges = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, blank=True)
    discount_applicable = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=None, null=True, blank=True)
    terms_and_conditions = models.CharField()
    upload_additional_files = models.FileField(blank=True, null=True)
    total_estimate_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    


    def save(self, *args, **kwargs):
        if not self.estimate_number:
            now = datetime.datetime.now()
            current_month = now.strftime('%m')
            current_year = now.strftime('%Y')

            prefix = f'EST-{current_month}-{current_year}-' #for the estimate number prefix

            with transaction.atomic():  #using transaction to lock the table and get the max number
                #Getting highest existing estimate number for current month and year
                max_estimate_number = Estimates.objects.filter(
                    estimate_number__startswith=prefix
                ) .aggregate(max_number=Max('estimate_number'))['max_number']

                if max_estimate_number: # Extracting the number part from the highest estimate number and increment it
                    max_number = int(max_estimate_number.split('-')[-1])
                    new_number = max_number+1
                else: new_number = 0
                new_estimate_number = f'{prefix}{new_number:02}' #Format new number, ensuring it has leading zeros (e.g., 01, 02, etc.)
                self.estimate_number = new_estimate_number

        super().save(*args, **kwargs)

    def __str__(self):
        return self.estimate_number
    
class EstimateItems(models.Model):
    id = models.AutoField(primary_key=True)
    estimate = models.ForeignKey(Estimates, on_delete=models.CASCADE) #testing
    name = models.ForeignKey(Item, on_delete=models.CASCADE)
    offered_quantity_to_customer = models.PositiveIntegerField()
    selling_price_proposed_to_customer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __int__(self):
        #return f'{self.estimate.estimate_number} - {self.product}'
        return self.id
        #return f'{self.product, self.selling_price_proposed_to_customer}'


# class EstimateItems(models.Model):
#     quoteitems_id = models.AutoField(primary_key=True)
#     estimate = models.ForeignKey(Estimates, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Item, on_delete=models.CASCADE)
#     offered_quantity_to_customer = models.PositiveIntegerField()
#     selling_price_proposed_to_customer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         #return f'{self.estimate.estimate_number} - {self.product}'
#         #return self.product
#         return f'{self.product, self.selling_price_proposed_to_customer}'

