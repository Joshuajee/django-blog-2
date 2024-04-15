from django.urls import path
from .views import index, latest, top, dummy

urlpatterns = [
    path("", index),
    path("latest", latest),
    path("top", top),
    path("dummy/", dummy)
]
