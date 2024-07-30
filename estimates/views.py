from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from estimates.models import Estimates, EstimateItems
from estimates.serializers import EstimateSerializer
from estimates.forms import EstimateForm

from django.template.response import SimpleTemplateResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

class EstimateListCreateView(generics.ListCreateAPIView):
    queryset = Estimates.objects.all()
    serializer_class = EstimateSerializer

class EstimateCreationView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'estimates/estimate_form.html'

    def get(self, request, id):
        # form = EstimateForm()
        # return render(request, 'estimates/estimate_form.html', {'form': form})
        estimate = get_object_or_404(Estimates, id=id)
        serializer = EstimateSerializer(estimate)
        return Response({'serializer': serializer, 'estimate': estimate})
        
    
    def post(self, request, id):
        # form = EstimateForm(request.POST)
        # if form.is_valid():
        #     estimate = form.save()
        #     serializer = EstimateSerializer(estimate)
        #     return redirect('estimate-pdf-creation')
        # return render(request, 'estimate_form.html', {'form': form})

        estimate = get_object_or_404(Estimates, pk=id)
        serializer = EstimateSerializer(estimate, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'estimate': estimate})
        serializer.save()
        return redirect('estimate-list-create')

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