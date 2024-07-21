from django.urls import path
from users.views import UserCreateView, UserUpdateView, register_user, user_login, user_logout


urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user-create'),
    path('update_user/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('register/', register_user, name='register_user'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
