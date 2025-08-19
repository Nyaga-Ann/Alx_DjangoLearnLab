from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.select_related('author')[:10]
    return render(request, "blog/index.html", {"posts": posts})
