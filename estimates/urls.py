from django.urls import path
from estimates.views import EstimateListCreateView, EstimateRetrieveUpdateDeleteView, estimate_pdf_creation_view, EstimateCreationView, EstimateDetailView, estimates_index


urlpatterns = [
    path('index/', EstimateListCreateView.as_view(), name='estimate-list-create'),
    path('<int:pk>/', EstimateRetrieveUpdateDeleteView.as_view(), name='estimate-retrieve-update-delete'),
    path('pdf/', estimate_pdf_creation_view, name='estimate-pdf-creation'),
    path('create_estimate/', EstimateCreationView.as_view(), name='create-estimate'),
    path('detail_estimate/<int:estimate_id>/', EstimateDetailView.as_view(), name='estimate-detail'),
    #path('index/', estimates_index, name='estimates-index'),
]
