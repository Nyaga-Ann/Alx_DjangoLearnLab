from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ProfileForm

def register_view(request):
    """User sign up using extended UserCreationForm with email."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created! You can now log in.")
            # Optionally auto-login:
            # login(request, user)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile_view(request):
    """View & edit basic profile fields."""
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "profile.html", {"form": form})

def home(request):
    posts = Post.objects.select_related('author')[:10]
    return render(request, "blog/index.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # create this later
    context_object_name = "posts"
