from django.shortcuts import render, HttpResponseRedirect
from .models import Post, User
from django.contrib.auth import authenticate, login, logout
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required

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
    
    post.views += 1
    
    post.save()
    
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
            if user == None:
                return render(req, "login.html", {
                    'error': "Wrong Username or Password"
                })
            else:
                login(req, user)
                try:
                    return HttpResponseRedirect(req.GET["next"])
                except:
                    return HttpResponseRedirect("/")
        except:
            pass
                
    return render(req, "login.html")

def logout_view(req):
    logout(req)
    return HttpResponseRedirect("/")


@login_required(login_url="/login")
def create_post(req):
    
    form = CreatePostForm()
    
    if req.method == "POST":
        
        form = CreatePostForm(req.POST)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            Post(user=req.user, title=title, content=content).save()
            
            return render(req, "create-post.html", {
                "form": form,
                "success": "Created Successfully"
            })
        else:
            return render(req, "create-post.html", {
                "form": form,
                "error": "Invalid Input"
            })
    
    return render(req, "create-post.html", {
        "form": form
    })
    
    
@login_required(login_url="/login")
def profile(req):
    return render(req, "profile.html")


@login_required(login_url="/login")
def upload_profile_img(req):
    
    if req.method == "POST":
        user = User.objects.get(id=req.user.id)
        print(req.FILES['profile-img'])
        user.profile_img = req.FILES['profile-img']
        user.save()
    
    return render(req, "profile.html", {
        
    })
    

@login_required(login_url="/login")
def my_blogs(req):
    
    posts = Post.objects.filter(user=req.user)
    
    return render(req, "index.html", {
        "posts": posts
    })

    