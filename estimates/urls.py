from django.urls import path
from estimates.views import EstimateListCreateView, EstimateRetrieveUpdateDeleteView, EstimateCreationView, EstimateDetailView, estimates_index, PdfGenerationView, ViewPDF, send_estimate_to_customer, check_estimate, accept_estimate, reject_estimate


urlpatterns = [
    path('index/', EstimateListCreateView.as_view(), name='estimate-list-create'),
    path('<int:pk>/', EstimateRetrieveUpdateDeleteView.as_view(), name='estimate-retrieve-update-delete'),
    #path('pdf/', estimate_pdf_creation_view, name='estimate-pdf-creation'),
    path('create_estimate/', EstimateCreationView.as_view(), name='create-estimate'),
    path('detail_estimate/<int:estimate_id>/', EstimateDetailView.as_view(), name='estimate-detail'),
    path('generate_pdf/<int:estimate_id>/', PdfGenerationView.as_view(), name='generate-pdf'),
    path('pdf_view/<int:estimate_id>/', ViewPDF.as_view(), name='pdf-view'),
    path('send_estimate/<int:estimate_id>/', send_estimate_to_customer, name='send-estimate'),
    #path('index/', estimates_index, name='estimates-index'),
    path('check_online/<int:estimate_id>/', check_estimate, name='check_online'),
    path('<int:estimate_id>/accept/', accept_estimate, name='accept_estimate'),
    path('<int:estimate_id>/reject/', reject_estimate, name='reject_estimate'),
]
