from django.db import models

# Create your models here.
class Start(models.Model):
    StartId = models.AutoField(primary_key=True)
    fname = models.CharField('First name' ,max_length = 100)
    lname = models.CharField('Last name' ,max_length = 100)
    business = models.CharField('Business Name' ,max_length = 100)
    address = models.CharField('Address' ,max_length = 100)
    state = models.CharField('State' ,max_length = 100)
    code = models.CharField('Code', max_length=6)