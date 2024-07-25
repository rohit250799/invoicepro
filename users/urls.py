from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.views import  RegisterView, LoginView, register_user, user_login, user_logout, siteIndex


urlpatterns = [
    path('', siteIndex, name='invoicepro index'),
    # path('create_user/', UserCreateView.as_view(), name='user-create'),
    # path('update_user/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('register_user/', RegisterView.as_view(), name='register-view'),
    path('login_user/', LoginView.as_view(), name='login-view'),
    path('register/', register_user, name='register_user'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
