from django.urls import path
from estimates.views import EstimateListCreateView, EstimateRetrieveUpdateDeleteView


urlpatterns = [
    path('', EstimateListCreateView.as_view(), name='estimate-list-create'),
    path('<int:pk>/', EstimateRetrieveUpdateDeleteView.as_view(), name='estimate-retrieve-update-delete'),
]
