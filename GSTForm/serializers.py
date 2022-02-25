from rest_framework import serializers
from .models import GST

class GSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = GST
        fields = ('GSTId',
                    'Fname', 
                    'Lname',
                    'GSTNo',
                    'Email',
                    'Phone',  
                    'Address', 
                    'State', 
                    'Code',
                    'Account')