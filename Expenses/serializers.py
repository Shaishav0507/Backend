from rest_framework import serializers
from Expenses.models import Expense 

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('ExpenseId',
                    'Category',
                    'Amount' )