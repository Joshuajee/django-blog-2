from django.urls import path
from .views import index, dummy

urlpatterns = [
    path("", index),
    path("dummy/", dummy)
]
