from django.shortcuts import render
from datetime import date

post_dic = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Simon",
        "date": date(2023, 8, 9),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua",
        "content": """
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
            invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
            At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
            no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
            consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
            magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea 
            rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Simon",
        "date": date(2023, 8, 9),
        "title": "Mountain Biking",
        "excerpt": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua",
        "content": """
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
            invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
            At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
            no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
            consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
            magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea 
            rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Simon",
        "date": date(2023, 8, 9),
        "title": "Mountain Running",
        "excerpt": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua",
        "content": """
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
            invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
            At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
            no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
            consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore 
            magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea 
            rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
        """
    },
    
]

# Create your views here.

def index(request):
    sorted_posts = sorted(post_dic, key=__get_date)
    
    latest_posts = sorted_posts[-3:]
    
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })

def posts(request):
    
    return render(request, "blog/all-posts.html", {
       "posts": post_dic, 
    })

def post_detail(request, slug):
    post = __get_post(post_dic, slug)
    return render(request, "blog/post-detail.html", {
        "post": post_dic
    })


## private function
def __get_date(post):
    return post["date"]

def __get_post(posts, title):
    return next((post for post in posts if post["title"] == title), None)