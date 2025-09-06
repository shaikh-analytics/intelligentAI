
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def service_detail(request):
    return render(request, 'service-details.html')

def portfolio(request):
    return render(request,'portfolio-details.html')