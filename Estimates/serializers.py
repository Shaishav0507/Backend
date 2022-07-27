from rest_framework import serializers
from .models import Estimate

class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields = ('EstimateId',
                    'EstimateNo', 
                    'Create',
                    'Update',
                    'Item',
                    'Price')