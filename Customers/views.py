from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Customers
from .serializers import *
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def customerApi(request, id=0):
    if request.method == 'GET':
        data = Customers.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        start_data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=start_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        start_data = JSONParser().parse(request)
        start = Customers.objects.get(CustomerId=start_data['CustomerId'])
        serializer = CustomerSerializer(start, data=start_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        data = Customers.objects.get(CustomerId=id)
        data.delete()
        return JsonResponse("Deleted Successfully !!", safe=False)
