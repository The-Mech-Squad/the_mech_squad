from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from orbital_decay.find import find_sat

def hal(request):
  return render(request, 'hal.html')


def homepage(request):
  return render(request, 'homepage.html')

def about(request):
  return render(request, 'about.html')

def handler404(request, exception=None):
  return render(request, '404.html')

def findSat(request):
  # request should be ajax and method should be GET.
  if request.is_ajax and request.method == "GET":
      # get the sat name from the client side.
    sat_name = request.GET.get("sat_name", None)
    print('-----')
    print(sat_name)
    find_sat(sat_name)
      # check for the sat name in the database.
      # if sat exists:
        # if nick_name found return not valid new friend
    return HttpResponse(status = 200)
      # else:
        # if nick_name not found, then user can create a new friend.
        # return JsonResponse({"valid":True}, status = 200)

  # return JsonResponse({}, status = 400)