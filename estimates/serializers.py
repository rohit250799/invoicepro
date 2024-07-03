from estimates.models import Estimates, EstimateItems
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from items.serializers import ItemSerializer
from items.models import Item
from customers.models import Customer

class EstimateItemSerializer(serializers.ModelSerializer):
    product = ItemSerializer()

    class Meta:
        model = EstimateItems
        fields = ['product', 'quantity', 'price']

class EstimateSerializer(serializers.ModelSerializer):
    items = EstimateItemSerializer(many=True)
    customer_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Estimates
        fields = ['id', 'estimate_number', 'estimate_date', 'offer_expiry_date', 'customer_id', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        customer_id = validated_data.pop('customer_id')
        customer = Customer.objects.get(id=customer_id)
        estimate = Estimates.objects.create(customer=customer, **validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            product, _ = Item.objects.get_or_create(**product_data)
            EstimateItems.objects.create(estimate=estimate, product=product, **item_data)
        return estimate

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        customer_id = validated_data.pop('customer_id')
        customer = Customer.objects.get(id=customer_id)
        instance.estimate_number = validated_data.get('estimate_number', instance.estimate_number)
        instance.date = validated_data.get('date', instance.date)
        instance.customer = customer
        instance.save()

        instance.items.all().delete()
        for item_data in items_data:
            product_data = item_data.pop('name')
            item, _ = Item.objects.get_or_create(**product_data)
            EstimateItems.objects.create(estimate=instance, item=item, **item_data)

        return instance
