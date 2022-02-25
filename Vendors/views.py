from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Vendors
from .serializers import *

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def vendorApi(request, id=0):
    if request.method == 'GET':
        data = Vendors.objects.all()
        serializer = VendorSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        start_data = JSONParser().parse(request)
        serializer = VendorSerializer(data=start_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        start_data = JSONParser().parse(request)
        start = Vendors.objects.get(VendorId=start_data['VendorId'])
        serializer = VendorSerializer(start, data=start_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        data = Vendors.objects.get(VendorId=id)
        data.delete()
        return JsonResponse("Deleted Successfully !!", safe=False)
