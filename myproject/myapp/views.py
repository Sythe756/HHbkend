from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Tools, SeedInventory, Inventory, Money
from .serializers import ToolsSerializer, SeedInventorySerializer, InventorySerializer, MoneySerializer
# Create your views here.

from django.http import JsonResponse
from .models import *
from .serializers import *
from django.http import HttpResponse

# says hello in http body
def hello(request):
    return HttpResponse("Hello, world.")
    

class Toollist(APIView):
    def get(self, request):
        tools = Tools.objects.all()
        serializer = ToolsSerializer(tools, many=True)
        return Response(serializer.data)

class Seedlist(APIView):
    def get(self, request):
        seeds = SeedInventory.objects.all()
        serializer = SeedInventorySerializer(seeds, many=True)
        return Response(serializer.data)

class Inventorylist(APIView):
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

class Moneylist(APIView):
    def get(self, request):
        money = Money.objects.all()
        serializer = MoneySerializer(money, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MoneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


