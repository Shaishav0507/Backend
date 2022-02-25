from django.db import models

# Create your models here.
class Expense(models.Model):
    ExpenseId = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)