
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hal/', views.hal),
    path('', views.homepage ),
    path('about/', views.about),
]
handler404 = views.handler404
urlpatterns += staticfiles_urlpatterns()
