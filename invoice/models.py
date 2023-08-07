from django.db import models
from uuid import uuid4
# Create your models here.
class Invoice(models.Model):
    id = models.UUIDField(
        editable=False,
        default=uuid4,
        primary_key=True
    )
    date = models.DateTimeField("Date",auto_now_add=True)
    invoice_no = models.IntegerField("Invoice Number",blank=False)
    customer_name = models.CharField("Customer Name",max_length=255,blank=False)


class Invoice_Detail(models.Model):
    invoice = models.OneToOneField(Invoice,on_delete=models.CASCADE,related_name='invoice_details',primary_key=True)
    description = models.TextField("Invoice description",blank=True,null=True)
    quantity = models.IntegerField("Quantity of items",blank=False,default=1)
    unit_price = models.FloatField("Unit Price",blank=False)
    @property
    def price(self):
        return self.unit_price*self.quantity
