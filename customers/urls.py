from django.urls import path
from customers.views import CustomerListCreateView, CustomerRetrieveUpdateDeleteView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name = 'customer-list-create'),
    path('<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name= 'customer-retrieve-update-delete'),
]
