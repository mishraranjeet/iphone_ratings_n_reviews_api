from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import DashboardSerialzer
from django.shortcuts import HttpResponse




def home(request):
    return HttpResponse("This is the API for Iphone ratings and reviews put /api to url to view api")

@api_view(['GET', 'POST','DELETE'])
def api_view(request):
    if request.method == 'GET':
        iphonedata = Iphone_Data.objects.all()
        serializer = DashboardSerialzer(iphonedata, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DashboardSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
