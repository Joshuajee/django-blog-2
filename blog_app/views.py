from django.shortcuts import render, HttpResponseRedirect
from .models import Post, User
from django.contrib.auth import authenticate, login, logout

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
    
def create_account(req):
    
    if req.method == "POST":
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email    = req.POST['email']
        password = req.POST['password']
        
        try:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            return HttpResponseRedirect("/")
        except:
            print("error")
            pass
    
    return render(req, "create-account.html")

def login_view(req):
    
    if req.method == "POST":
        
        username = req.POST['username']
        password = req.POST['password']
        
        try:
            user = authenticate(username=username, password=password)
            print(user)
            if user == None:
                return render(req, "login.html", {
                    'error': "Wrong Username or Password"
                })
            else:
                login(req, user)
                return HttpResponseRedirect("/")
        except:
            pass
                
    return render(req, "login.html")

def logout_view(req):
    logout(req)
    return HttpResponseRedirect("/")