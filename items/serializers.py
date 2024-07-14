import warnings
from items.models import Item
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields = ['name', 'item_type', 'description', 'marked_price_by_user_for_sale', 'available_stock']
        fields = '__all__'

    def validate(self, data):
        if data['available_stock'] <= data['inventory_threshold_quantity']:
            warnings.warn('Available stock has crossed inventory threshold quantity. Time to restock')
        
        if data['item_type'] == 'SERVICES': 
            data['available_stock'] = None
            data['inventory_threshold_quantity'] = 0

        if not data['taxes_applicable'] and data['tax_percentage_on_item']: 
            raise serializers.ValidationError({'tax_percentage_on_item': 'if taxes applicable is false, tax percentage is not applicable'})

        if data['taxes_applicable'] and not data['tax_percentage_on_item']: 
            raise serializers.ValidationError({'tax_percentage_on_item': 'if taxes applicable is true, tax percentage is mandatory'})  
        
        return data
    