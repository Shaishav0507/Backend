from django.db import models

# Create your models here.
class Vendors(models.Model):
    VendorId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    GST = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Pan = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Bank = models.CharField(max_length=100)
    