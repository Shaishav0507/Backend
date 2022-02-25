from rest_framework import serializers
from Customers.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('CustomerId',
                    'Name',
                    'Address',
                    'GST',
                    'Email',
                    'Pan',
                    'Contact',
                    'Bank')