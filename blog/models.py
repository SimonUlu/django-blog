from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=100)
    
    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    
    def __full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.__full_name()


class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    
    
    def __str__(self):
        return f"{self.title}"
    
    
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")