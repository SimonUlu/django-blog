from django.contrib import admin
from .models import Post, Tag, Author, Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date" ,"author")
    prepopulated_fields = {"slug": ("title",)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "text")

# Register your models here.

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)

admin.site.register(Author)

admin.site.register(Comment, CommentAdmin)
