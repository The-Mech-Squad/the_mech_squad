from django.http import HttpResponse
from django.shortcuts import render

def hal(request):
  return render(request, 'hal.html')


def homepage(request):
  return render(request, 'homepage.html')

def about(request):
  return render(request, 'about.html')

def handler404(request, exception=None):
  return render(request, '404.html')

  
