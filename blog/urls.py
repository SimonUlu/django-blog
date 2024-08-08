from django.urls import path
from . import views
from .views import IndexView, AllPostsView

urlpatterns = [
    path("", IndexView.as_view(), name="starting-page"),
    path("posts", AllPostsView.as_view(), name="posts-page"), 
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]