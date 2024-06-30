from estimates.models import Estimates
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimates
        fields = '__all__'

    