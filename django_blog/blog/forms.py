# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from .models import Post, Comment, Tag

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Add tags separated by commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Handle tags
        tags_str = self.cleaned_data.get("tags", "")
        if tags_str:
            tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']