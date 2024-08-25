from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.html import strip_tags
from django.http import HttpResponse, Http404
from django.core.mail import EmailMessage
from rest_framework import generics, viewsets, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response 
from reportlab.lib.pagesizes import letter
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from estimates.models import Estimates, EstimateItems
from estimates.serializers import EstimateSerializer
from estimates.forms import EstimateForm

from io import BytesIO
from django.http import FileResponse
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa

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

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    #pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    pdf = pisa.pisaDocument(html, result)
    #pdf = pisa.CreatePDF(html, dest=result)


    if not pdf.err: return HttpResponse(result.getvalue(), content_type = 'application/pdf')
        #return result.getvalue()
    return None

    
class ViewPDF(View):
    def get(self, request, estimate_id, *args, **kwargs):
        estimate_concerned = Estimates.objects.get(pk=estimate_id)
        estimate_data = {
            estimate_concerned.estimate_id: {
                'estimate_number': estimate_concerned.estimate_number,
                'customer': estimate_concerned.customer,
                'estimate_date': estimate_concerned.estimate_date,
                'offer_expiry_date': estimate_concerned.offer_expiry_date,
                'subject': estimate_concerned.subject,
                'status': estimate_concerned.status,
                'customer_notes': estimate_concerned.customer_notes,
                'tax_from_source_type': estimate_concerned.tax_from_source_type,
                'applicable_tax_percentage': estimate_concerned.applicable_tax_percentage,
                'shipping_charges_applicable': estimate_concerned.shipping_charges_applicable,
                'shipping_charges': estimate_concerned.spipping_charges,
                'discount_applicable': estimate_concerned.discount_applicable,
                'discount_percentage': estimate_concerned.discount_percentage,
                'terms_and_conditions': estimate_concerned.terms_and_conditions,
                'upload_additional_files': estimate_concerned.upload_additional_files,
                'total_estimate_amount': estimate_concerned.total_estimate_amount            
            }
        }
        
        #pdf = render_to_pdf('estimates/estimate_pdf_template.html', {'estimates': estimate_data})
        #pdf = render_to_pdf('estimates/estimate_pdf_template.html', {'estimates': 'estimate_data'})
        pdf = render_to_pdf('estimates/estimate_pdf_template.html', {'estimates': estimate_data})

        # pdf = render_to_pdf(estimate_id)
        # if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
        #     #response = HttpResponse(pdf, content_type='application/pdf')
        #     response = HttpResponse(content_type='application/pdf')
        #     response['Content-Disposition'] = 'attachment; filename="my_estimate.pdf"'
        #     return response
        # return HttpResponse("Error generating PDF", status=400)

def render_pdf_for_sending(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    #pdf = pisa.pisaDocument(result)
    pdf = pisa.pisaDocument(result)
    



    if not pdf.err: #return HttpResponse(result.getvalue(), content_type = 'application/pdf')
        return result.getvalue()
    return None

@csrf_exempt    
def send_estimate_to_customer(self, estimate_id):
    subject = f"New estimate {'estimate_number'} sent by Tester"
    estimate_used = Estimates.objects.get(pk=estimate_id)
    estimate_data = {
            estimate_used.estimate_id: {
                'estimate_number': estimate_used.estimate_number,
                'customer': estimate_used.customer,
                'estimate_date': estimate_used.estimate_date,
                'offer_expiry_date': estimate_used.offer_expiry_date,
                'subject': estimate_used.subject,
                'status': estimate_used.status,
                'customer_notes': estimate_used.customer_notes,
                'tax_from_source_type': estimate_used.tax_from_source_type,
                'applicable_tax_percentage': estimate_used.applicable_tax_percentage,
                'shipping_charges_applicable': estimate_used.shipping_charges_applicable,
                'shipping_charges': estimate_used.spipping_charges,
                'discount_applicable': estimate_used.discount_applicable,
                'discount_percentage': estimate_used.discount_percentage,
                'terms_and_conditions': estimate_used.terms_and_conditions,
                'upload_additional_files': estimate_used.upload_additional_files,
                'total_estimate_amount': estimate_used.total_estimate_amount            
            }
        }
    pdf = render_pdf_for_sending('estimates/estimate_pdf_template.html', {'estimates': 'estimate_data'})

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="my_estimate.pdf"'
        #return response
    from_email = 'from@yourdjangoapp.com'
    to = 'to@yourbestuser.com'

    message = EmailMessage(subject=subject, body=pdf, from_email=from_email, to=(to, ))
    message.attach('my_estimate.pdf', pdf, 'application/pdf')
    message.send()
    return HttpResponse(status=status.HTTP_200_OK)

def estimates_index(request):
    return render(request, 'estimates/estimates_list.html')









