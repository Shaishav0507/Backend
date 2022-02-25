from rest_framework import serializers
from Invoice.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('InvoiceId',
                    'Name',
                    'Invoice_no',
                    'Invoice_Date',
                    'Payment_Date',
                    'Amount', )