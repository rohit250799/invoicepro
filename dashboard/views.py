from django.shortcuts import render

# Create your views here.

def siteIndex(request):
    return render(request, 'dashboard/index.html')