from rest_framework import serializers
from Vendors.models import Vendors

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ('VendorId',
                    'Name',
                    'Address',
                    'GST',
                    'Email',
                    'Pan',
                    'Contact',
                    'Bank')