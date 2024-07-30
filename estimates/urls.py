from django.urls import path
from estimates.views import EstimateListCreateView, EstimateRetrieveUpdateDeleteView, estimate_pdf_creation_view


urlpatterns = [
    path('', EstimateListCreateView.as_view(), name='estimate-list-create'),
    path('<int:pk>/', EstimateRetrieveUpdateDeleteView.as_view(), name='estimate-retrieve-update-delete'),
    path('pdf/', estimate_pdf_creation_view, name='estimate-pdf-creation'),
]
