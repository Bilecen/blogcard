from django.urls import path, include
from .views import index as home

urlpatterns = [
    path('', home, name="index")
]
