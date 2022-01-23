from importlib.resources import path

from base import views
from .views import home

urlpatterns = [
    path('', views.home),
]
