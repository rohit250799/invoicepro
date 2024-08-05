from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, viewsets, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from estimates.models import Estimates, EstimateItems
from estimates.serializers import EstimateSerializer
from estimates.forms import EstimateForm

#from django.template.response import SimpleTemplateResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

class EstimateListCreateView(generics.ListCreateAPIView):
    queryset = Estimates.objects.all()
    serializer_class = EstimateSerializer

class EstimateCreationView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer]
    template_name = 'estimates/estimate_form.html'
    
    def post(self, request):
        data = request.data
        serializer = EstimateSerializer(data=data)
        #print(serializer.data)
        if serializer.is_valid():
            #input_data = serializer.validated_data
            serializer.save()
            return Response({'serializer': serializer})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class EstimateDetailView(APIView):
    def get(self, request, estimate_id, *args, **kwargs):
        try:
            estimate = Estimates.objects.get(pk=estimate_id)
        except Estimates.DoesNotExist:
            return Response({"error": "Estimate not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EstimateSerializer(estimate)
        return Response(serializer.data)

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









