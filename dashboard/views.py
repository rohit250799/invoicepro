from django.shortcuts import render

# Create your views here.

def siteIndex(request):
    return render(request, 'dashboard/index.html')

def login_redirection(request):
    return render(request, 'dashboard/dashboard.html')