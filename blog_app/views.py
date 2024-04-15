from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, "index.html")

def latest(req):
    return render(req, "index.html")

def top(req):
    return render(req, "index.html")

def dummy(req):
    return render(req, "dummy.html")


