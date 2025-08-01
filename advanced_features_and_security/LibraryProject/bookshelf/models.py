from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField() 
    
    def __str__(self):
        return self.title
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username 

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view", "Can view article"),
            ("can_create", "Can create article"),
            ("can_edit", "Can edit article"),
            ("can_delete", "Can delete article"),
        ]