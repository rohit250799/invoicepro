from estimates.models import Estimates, EstimateItems
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from items.serializers import ItemSerializer
from items.models import Item
from customers.models import Customer

class EstimateItemSerializer(serializers.ModelSerializer):
    #product = ItemSerializer()

    class Meta:
        model = EstimateItems
        #fields = ['quoteitems_id', 'product', 'offered_quantity_to_customer', 'selling_price_proposed_to_customer']
        fields = ['name', 'offered_quantity_to_customer', 'selling_price_proposed_to_customer']


class EstimateSerializer(serializers.ModelSerializer):
    items = EstimateItemSerializer(many=True)
    #offered_estimate_items = EstimateItemSerializer(many=True)

    
    class Meta:
        model = Estimates
        fields = ['estimate_number', 'customer', 'estimate_date', 'offer_expiry_date', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        estimate = Estimates.objects.create(**validated_data)
        #items_data = estimate.items.all()
        # Handle each item in the items_data
        #item_ids = [item_data['quoteitems_id'] for item_data in items_data]  # Extract IDs from the item data
        for item_data in items_data:
            #item_id = EstimateItems.objects.get(product=item_data['product'].id) - testing with below line
            item = Item.objects.get(id=item_data['name'].id)
            #item = Item.objects.create(estimate=estimate, **item_data)
            # item, created = Item.objects.get_or_create(
            #     name=item_data['product'],
            #     defaults={
            #         'price': item_data.get('selling_price_proposed_to_customer', 1.0),
            #     }
            # ) - testing (latest)
            offered_quantity_to_customer = item_data.get('offered_quantity_to_customer', 1)
            #offered_quantity_to_customer = item_data['offered_quantity_to_customer']

            #selling_price_proposed_to_customer = item_data.get('selling_price_proposed_to_customer', 1)
            #selling_price_proposed_to_customer = item_data['selling_price_proposed_to_customer']


            #estimate.offered_estimate_items.add(item) - test
            #EstimateItems.objects.create(estimate=estimate, **item_data)
        # estimate.items.set(item_ids)

        #estimate.items.set(items_data) #testing

        #creating EstimateItems object with imp fields
            EstimateItems.objects.create(
                estimate=estimate, name     =item, offered_quantity_to_customer=offered_quantity_to_customer,
                selling_price_proposed_to_customer=item_data.get('selling_price_proposed_to_customer', 1.0)
            )

        return estimate

    # def update(self, instance, validated_data):
    #     items_data = validated_data.pop('items')
    #     customer_id = validated_data.pop('customer_id')
    #     customer = Customer.objects.get(id=customer_id)
    #     instance.estimate_number = validated_data.get('estimate_number', instance.estimate_number)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.customer = customer
    #     instance.save()

    #     instance.items.all().delete()
    #     for item_data in items_data:
    #         product_data = item_data.pop('name')
    #         item, _ = Item.objects.get_or_create(**product_data)
    #         EstimateItems.objects.create(estimate=instance, item=item, **item_data)

    #     return instance
    
    def validate(self, data):
        if data['estimate_date'] > data['offer_expiry_date']:
            raise serializers.ValidationError({'offer_expiry_date': 'the expiry date cannot be earlier than estimate date'})
        return data
