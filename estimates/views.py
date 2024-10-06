import ast #testing
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.html import strip_tags
from django.http import HttpResponse, Http404
from django.urls import reverse
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
    #items = queryset.items.all() #testing
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
        estimate_items = estimate.items.all()
        response['Content-Disposition'] = 'attachment; filename="estimate.pdf"'
        html_string = render_to_string('estimates/estimate_pdf_template.html', {
            'estimate_number': estimate.estimate_number,  
            'title': 'Test title',
            'content': 'Test content',
            'estimate_items': estimate_items
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
    pdf = pisa.pisaDocument(html, result)
    
    if not pdf.err: return HttpResponse(result.getvalue(), content_type = 'application/pdf')
    return None

    
class ViewPDF(View):
    def get(self, request, estimate_id, *args, **kwargs):
        estimate_concerned = Estimates.objects.get(pk=estimate_id)
        estimate_concerned_items = estimate_concerned.items.all()
        estimate_data = {
            estimate_concerned.estimate_id: {
                'estimate_number': estimate_concerned.estimate_number,
                'customer': estimate_concerned.customer,
                'estimate_date': estimate_concerned.estimate_date,
                'offer_expiry_date': estimate_concerned.offer_expiry_date,
                'subject': estimate_concerned.subject,
                'status': estimate_concerned.status,
                'items': estimate_concerned_items, #for testing
                'customer_notes': estimate_concerned.customer_notes,
                'tax_from_source_type': estimate_concerned.tax_from_source_type,
                'applicable_tax_percentage': estimate_concerned.applicable_tax_percentage,
                'shipping_charges_applicable': estimate_concerned.shipping_charges_applicable,
                'shipping_charges': estimate_concerned.shipping_charges,
                'discount_applicable': estimate_concerned.discount_applicable,
                'discount_percentage': estimate_concerned.discount_percentage,
                'terms_and_conditions': estimate_concerned.terms_and_conditions,
                'upload_additional_files': estimate_concerned.upload_additional_files,
                'total_estimate_amount': estimate_concerned.total_estimate_amount            
            }
        }
        
        pdf = render_to_pdf('estimates/estimate_pdf_template.html', {'estimates': estimate_data})
        return HttpResponse(pdf, content_type='application/pdf')
        
def render_pdf_for_sending(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    



    if not pdf.err: return result.getvalue()
    return None

@csrf_exempt    
def send_estimate_to_customer(request, estimate_id):
    estimate_used = Estimates.objects.get(pk=estimate_id)
    subject = f"New estimate {estimate_used.estimate_number} sent by Tester"
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
            'shipping_charges': estimate_used.shipping_charges,
            'discount_applicable': estimate_used.discount_applicable,
            'discount_percentage': estimate_used.discount_percentage,
            'terms_and_conditions': estimate_used.terms_and_conditions,
            'upload_additional_files': estimate_used.upload_additional_files,
            'total_estimate_amount': estimate_used.total_estimate_amount            
        }
    }
    
    pdf = render_pdf_for_sending('estimates/estimate_pdf_template.html', {'estimates': estimate_data})

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="my_estimate.pdf"'
        relative_url = reverse('check_online', kwargs={'estimate_id': estimate_id})
        absolute_url = request.build_absolute_uri(relative_url)

        email_context = {
            'check_online': absolute_url,
            'estimate_id': estimate_used.estimate_id,
            'estimate_data_for_email_context': estimate_data

        }
        email_html_content = render_to_string('estimates/mail_template.html', email_context)

        
    from_email = 'from@yourdjangoapp.com'
    to = 'to@yourbestuser.com'

    message = EmailMessage(subject=subject, body=email_html_content, from_email=from_email, to=(to, ))
    
    message.content_subtype = 'html'

    message.attach('my_estimate.pdf', pdf, 'application/pdf')
    message.send()

    return HttpResponse("Email sent succesfully", status=status.HTTP_200_OK)

def estimates_index(request):
    return render(request, 'estimates/estimates_list.html')


def check_estimate(request, estimate_id):
    estimate_received = Estimates.objects.get(pk=estimate_id)
    received_estimate_data = {
        estimate_received.estimate_id: {
                'estimate_number': estimate_received.estimate_number,
                'customer': estimate_received.customer,
                'estimate_date': estimate_received.estimate_date,
                'offer_expiry_date': estimate_received.offer_expiry_date,
                'subject': estimate_received.subject,
                'status': estimate_received.status,
                'customer_notes': estimate_received.customer_notes,
                'tax_from_source_type': estimate_received.tax_from_source_type,
                'applicable_tax_percentage': estimate_received.applicable_tax_percentage,
                'shipping_charges_applicable': estimate_received.shipping_charges_applicable,
                'shipping_charges': estimate_received.shipping_charges,
                'discount_applicable': estimate_received.discount_applicable,
                'discount_percentage': estimate_received.discount_percentage,
                'terms_and_conditions': estimate_received.terms_and_conditions,
                'upload_additional_files': estimate_received.upload_additional_files,
                'total_estimate_amount': estimate_received.total_estimate_amount            
            }      
        }
    return render(request, 'estimates/estimate_page.html', received_estimate_data)

def accept_estimate(request, estimate_id):
    # Logic to accept the offer
    return HttpResponse("Offer accepted.")

def reject_estimate(request, estimate_id):
    # Logic to reject the offer
    return HttpResponse("Offer rejected.")





