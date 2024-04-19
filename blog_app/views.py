from django.shortcuts import render
from .models import Post

# Create your views here.

def index(req):
    posts = Post.objects.all()
    return render(req, "index.html", {
        "posts": posts
    })

def latest(req):
    posts = Post.objects.all().order_by("-date")
    return render(req, "index.html", {
        'posts': posts
    })

def top(req):
    posts = Post.objects.all().order_by("-views")
    return render(req, "index.html", {
        "posts": posts
    })
    
def post(req, slug):
    
    post = Post.objects.get(slug=slug)
    
    return render(req, "post.html", {
        "post" : post
    })

def dummy(req):
    return render(req, "dummy.html")


