from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserCreateView(generics.ListCreateAPIView):
#      model = 
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

