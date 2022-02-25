from django.db import models

# Create your models here.
class Invoice(models.Model):
    InvoiceId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Invoice_no = models.CharField(max_length=100)
    Invoice_Date = models.DateField()
    Payment_Date = models.DateField()
    Amount = models.CharField(max_length=100)