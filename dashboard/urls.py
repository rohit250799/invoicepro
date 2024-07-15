from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import siteIndex

urlpatterns = [
    path('', siteIndex, name='invoicepro index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
