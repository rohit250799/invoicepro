from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.html import strip_tags
from django.http import HttpResponse
from rest_framework import generics, viewsets, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response 
from reportlab.lib.pagesizes import letter
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from estimates.models import Estimates, EstimateItems
from estimates.serializers import EstimateSerializer
from estimates.forms import EstimateForm

#from django.template.response import SimpleTemplateResponse
import io
from django.http import FileResponse
from django.template.loader import render_to_string
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
        serializer = EstimateSerializer(data=request.data)
        #print(serializer.data)
        if serializer.is_valid():
            #input_data = serializer.validated_data
            serializer.save()
            #return Response({'serializer': self.serializer.data}, template_name='estimate_form.html')
            queryset = Estimates.objects.all()
            return Response({
                'estimate': queryset,
                'message': 'Estimate succesfully created',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        queryset = Estimates.objects.all()
        return Response({'estimates': queryset})

    
    
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

class PdfGenerationView(View):
    def get(self, request, estimate_id, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        estimate = Estimates.objects.get(pk=estimate_id)
        response['Content-Disposition'] = 'attachment; filename="estimate.pdf"'
        html_string = render_to_string('estimates/estimate_pdf_template.html', {
            'estimate_number': estimate.estimate_number,  
            # 'customer': 11,
            # 'estimate_date': '2024-08-12',
            # 'offer_expiry_date': '2024-08-19',
            'title': 'Test title',
            'content': 'Test content'
        })
        text_content = strip_tags(html_string)

        p = canvas.Canvas(response, pagesize=letter)
        p.drawString(30, 350, text_content)
        p.showPage()
        p.save()
        return response

def estimate_pdf_creation_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, 'Testing pdf creation')
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='estimate.pdf')

def estimates_index(request):
    return render(request, 'estimates/estimates_list.html')









