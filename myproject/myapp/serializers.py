from rest_framework import serializers
from .models import Tools, SeedInventory, Inventory, Money

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'
    
class SeedInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedInventory
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
    

class MoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = '__all__'
    
