from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from datetime import date
from .models import Post, Author, Tag
from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .forms import CommentForm

from django.views import View


# Create your views here.


class IndexView(View):

    def get(self, request):

        posts = Post.objects.all().order_by("-date")[:3]

        return render(
            request,
            "blog/index.html",
            {
                "posts": posts,
            },
        )


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "form": CommentForm(),
            "comments": post.comments.all(),
        }

        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(
                commit=False
            )  ## calling save will not directly hit database
            comment.posts = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "form": CommentForm(),
            "comments": post.comments.all(),
        }

        return render(request, "blog/post-detail.html", context)
