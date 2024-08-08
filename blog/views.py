from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag


# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-date")[:3]
    
    return render(request, "blog/index.html", {
        "posts": posts,
    })

def posts(request):
    
    posts = Post.objects.all()
    
    return render(request, "blog/all-posts.html", {
       "posts": posts, 
    })

def post_detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": post
    })

