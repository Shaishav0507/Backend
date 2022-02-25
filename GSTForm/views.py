from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import GST
from .serializers import *

# Create your views here.

@csrf_exempt
def GSTApi(request, id=0):
    if request.method == 'GET':
        data = GST.objects.all()
        serializer = GSTSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        start_data = JSONParser().parse(request)
        serializer = GSTSerializer(data=start_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        start_data = JSONParser().parse(request)
        start = GST.objects.get(GSTId=start_data['GSTId'])
        serializer = GSTSerializer(start, data=start_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        data = GST.objects.get(GSTId=id)
        data.delete()
        return JsonResponse("Deleted Successfully !!", safe=False)