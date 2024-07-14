from django.shortcuts import render

# Create your views here.

def dashboardIndex(request):
    return render(request, 'dashboard/base.html')