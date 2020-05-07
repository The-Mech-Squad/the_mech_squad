
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from orbital_decay.views import findSat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showcase/', include('showcase.urls')),
    path('hal/', views.hal),
    path('', views.homepage ),
    path('about/', views.about),
    path('hal/find/satellite', findSat, name = "find_sat")
]
handler404 = views.handler404
urlpatterns += staticfiles_urlpatterns()
