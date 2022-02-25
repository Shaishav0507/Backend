from django.db import models

# Create your models here.
class GST(models.Model):
    GSTId = models.AutoField(primary_key=True)
    Fname = models.CharField('First name' ,max_length = 100)
    Lname = models.CharField('Last name' ,max_length = 100)
    GSTNo = models.CharField('GSTNo' ,max_length = 100)
    Email = models.CharField('Email', max_length=50)
    Phone = models.CharField('Phone', max_length=15)
    Address = models.CharField('Address', max_length=100)
    State = models.CharField('State' ,max_length = 100)
    Code = models.CharField('Code', max_length=6)
    Account = models.CharField('Account', max_length=100)
    