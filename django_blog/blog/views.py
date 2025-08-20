from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def home(request):
    posts = Post.objects.select_related('author')[:10]
    return render(request, "blog/index.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # create this later
    context_object_name = "posts"
