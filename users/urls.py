from django.urls import path
from users.views import UserCreateView, UserUpdateView

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user-create'),
    path('update_user/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]
