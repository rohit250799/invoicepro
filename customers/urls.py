from django.urls import path
from .views import CustomerListCreateView, CustomerRetrieveUpdateView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name = 'customer-list-create'),
    path('<int:pk>/', CustomerRetrieveUpdateView.as_view(), name= 'customer-retrieve-update'),
]
