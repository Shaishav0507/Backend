
from django.db import models

# Create your models here.
class Estimate(models.Model):
    EstimateId = models.AutoField(primary_key=True)
    EstimateNo = models.CharField('Estimate No.' ,max_length = 100)
    Create = models.CharField('Create' ,max_length = 100)
    Update = models.CharField('Update' ,max_length = 100)
    Item = models.CharField('Item', max_length=50)
    Price = models.CharField('Price', max_length=15)