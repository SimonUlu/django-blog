from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag
from django.views import View
from django.views.generic import ListView


# Create your views here.

class IndexView(View):
    
    def get(self, request):

        posts = Post.objects.all().order_by("-date")[:3]
        
        return render(request, "blog/index.html", {
            "posts": posts,
        })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post  
    ordering = ["-date"]
    context_object_name = "all_posts"
    


def post_detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": post
    })

