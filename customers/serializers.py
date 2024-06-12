from .models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_gstin_representation(self, instance):
        representation = super().to_gstin_representation(instance)
        if instance.gst_treatment != Customer.GstTreatment.REGISTERED:
            representation.pop('gstin', None)
        return representation
    
    def validate(self, data):
        if data.get('gst_treatment') == Customer.GstTreatment.REGISTERED and not data.get('gstin'):
            raise serializers.ValidationError('GSTIN is required if GST Treatment is registered.')
        return data