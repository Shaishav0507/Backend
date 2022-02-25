from rest_framework import serializers
from .models import Start

class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = ('StartId',
                    'fname', 
                    'lname', 
                    'business', 
                    'address', 
                    'state', 
                    'code')