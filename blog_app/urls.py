from django.urls import path
from .views import index, latest, top, post, create_account, login_view, logout_view, create_post

urlpatterns = [
    path("", index),
    path("latest", latest),
    path("top", top),
    path("post/<slug:slug>", post),
    path("create", create_account),
    path("login", login_view),
    path("logout", logout_view),
    path("create-post", create_post)
]
