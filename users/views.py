from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from users.serializers import UserSerializer
from users.models import UserProfileInfo

#from django.contrib.auth import authenticate, login
#from django.http import HttpResponse, response
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

def siteIndex(request):
    return render(request, 'dashboard/index.html')

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #request.status_code = 201
            messages.success(request, 'User created succesfully!')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try: 
                user = UserProfileInfo.objects.get(email=username)
            except ObjectDoesNotExist: pass
        
        if not user: user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            messages.success(request, 'User logged in')
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def user_logout(request):
    if request.method == 'POST':
        try: 
            request.user.auth_token.delete()
            return Response({'message': 'Succesfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class UserCreateView(generics.CreateAPIView):
#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserProfileInfo.objects.filter(email=email).first()

        if user is None: 
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        return Response({
            'message': 'success'
        })    
