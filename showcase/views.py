from django.shortcuts import render

# Create your views here.
def showcase(request):
  return render(request, 'showcase/kinda_workin.html')