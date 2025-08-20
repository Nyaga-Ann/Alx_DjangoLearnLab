# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView, register_view, profile_view

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]

