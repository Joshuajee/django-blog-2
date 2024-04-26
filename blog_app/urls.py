from django.urls import path
from .views import index, latest, top, post, create_account, login_view, logout_view, create_post, my_blogs, profile, upload_profile_img
import blog_app.views
urlpatterns = [
    path("", index),
    path("latest", latest),
    path("top", top),
    path("post/<slug:slug>", post),
    path("create", create_account),
    path("login", login_view),
    path("logout", logout_view),
    path("create-post", create_post),
    path("my-blogs", my_blogs),
    path("profile", profile),
    path("upload", upload_profile_img)
]
