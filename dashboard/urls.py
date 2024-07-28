from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import siteIndex, login_redirection

urlpatterns = [
    path('', siteIndex, name='invoicepro index'),
    path('user_dashboard/', login_redirection, name='login-redirection'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
