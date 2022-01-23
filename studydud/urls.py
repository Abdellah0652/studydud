from importlib.resources import path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include

from base import views




urlpatterns = [
    path('admin/', admin.site.urls),

    path('base/', include('base.urls')),
]
