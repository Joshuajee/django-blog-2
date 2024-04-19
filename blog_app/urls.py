from django.urls import path
from .views import index, latest, top, post, dummy

urlpatterns = [
    path("", index),
    path("latest", latest),
    path("top", top),
    path("post/<slug:slug>", post),
    path("dummy/", dummy)
]
