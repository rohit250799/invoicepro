from customers.models import Customer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    GST_TREATMENT_CHOICES = (  
        ("Unregistered", "UNREGISTERED"),  
        ("Registered", "REGISTERED"),
    )
    
    gst_treatment = serializers.ChoiceField(GST_TREATMENT_CHOICES)
    gstin = serializers.CharField(max_length = 15, allow_blank=True, validators=[
        UniqueValidator(queryset=Customer.objects.all(), message='Provided gstin already exists')
    ])

    def validate(self, data):
        if data['gst_treatment'] == 'Registered' and not data['gstin']:
            raise serializers.ValidationError({'gstin': 'for Registered entities, gstin is mandatory'})

        if data['gst_treatment'] == 'Unregistered' and data['gstin']:
            raise serializers.ValidationError({'gstin': 'for Unregistered entities, gstin is not allowed'})
        return data
    
        
    