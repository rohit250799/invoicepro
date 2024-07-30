from django.shortcuts import render
from rest_framework import generics, viewsets
from estimates.models import Estimates, EstimateItems
from .serializers import EstimateSerializer

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

class EstimateListCreateView(generics.ListCreateAPIView):
    queryset = Estimates.objects.all()
    serializer_class = EstimateSerializer

class EstimateRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimates.objects.all()
    serializer_class= EstimateSerializer

class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimates.objects.all()
    serializer_class = EstimateSerializer

def estimate_pdf_creation_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, 'Testing pdf creation')
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='estimate.pdf')