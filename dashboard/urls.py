from django.urls import path
from dashboard.views import dashboardIndex

urlpatterns = [
    path('', dashboardIndex, name='dashboard index'),
]
