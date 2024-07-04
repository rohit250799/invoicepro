from items.models import Item
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'item_type', 'description', 'marked_price_by_user_for_sale', 'available_stock']

    