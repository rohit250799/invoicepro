from estimates.models import Estimates, EstimateItems
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from items.serializers import ItemSerializer
from items.models import Item

class EstimateItemSerializer(serializers.ModelSerializer):
    product = ItemSerializer()

    class Meta:
        model = EstimateItems
        fields = ['item', 'quantity', 'price']

class EstimateSerializer(serializers.ModelSerializer):
    items = EstimateItemSerializer(many=True)
    class Meta:
        model = Estimates
        fields = ['id', 'estimate_number', 'estimate_date', 'offer_expiry_date', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        estimate = Estimates.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            product, _ = Item.objects.get_or_create(**product_data)[0]
            EstimateItems.objects.create(estimate=estimate, product=product, **item_data)
        return estimate
    items = EstimateItemSerializer(many=True)
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.estimate_number = validated_data.get('estimate_number', instance.estimate_number)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        for item_data in items_data:
            product_data = item_data.pop('name')
            product, _ = Item.objects.get_or_create(**product_data)
            estimate_item, created = EstimateItems.objects.get_or_create(invoice=instance, product=product, defaults=item_data)
            if not created:
                item_data.quantity = item_data.get('quantity', estimate_item.quantity)
                estimate_item.price = item_data.get('price', estimate_item.price)
                estimate_item.save()

        return instance
