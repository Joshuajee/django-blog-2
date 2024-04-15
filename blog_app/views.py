from django.shortcuts import render
from .models import Post

# Create your views here.

def index(req):
    posts = Post.objects.all()
    return render(req, "index.html", {
        "posts": posts
    })

def latest(req):
    return render(req, "index.html")

def top(req):
    return render(req, "index.html")

def dummy(req):
    return render(req, "dummy.html")


