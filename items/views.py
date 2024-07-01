from django.shortcuts import render
from rest_framework import generics, viewsets
from items.models import Item
from items.serializers import ItemSerializer
from estimates.serializers import EstimateSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer   

class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = EstimateSerializer

