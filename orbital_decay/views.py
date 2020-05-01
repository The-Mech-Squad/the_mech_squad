from django.http import HttpResponse
from django.shortcuts import render

def hal(request):
  return render(request, 'hal.html')


def homepage(request):

  return render(request, 'spacegraph.html')
