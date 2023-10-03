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
    

def tools_list(request):
    tools = Tools.objects.all()
    toolsSerializer = ToolsSerializer(tools, many=True)
    return JsonResponse(toolsSerializer.data, safe=False)

def seeds_list(request):
    seeds = SeedInventory.objects.all()
    seedsSerializer = SeedInventorySerializer(seeds, many=True)
    return JsonResponse(seedsSerializer.data, safe=False)

def inventory_list(request):
    inventory = Inventory.objects.all()
    inventorySerializer = InventorySerializer(inventory, many=True)
    return JsonResponse(inventorySerializer.data, safe=False)

def money_list(request):
    money = Money.objects.all()
    moneySerializer = MoneySerializer(money, many=True)
    return JsonResponse(moneySerializer.data, safe=False)
