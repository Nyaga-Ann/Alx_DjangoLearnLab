from django.db import models
from django.conf import settings

class Post(models.Model):
    """
    Simple blog post model:
    - title: short title of the post
    - content: full text content
    - published_date: auto timestamp when created
    - author: FK to the user who wrote the post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title
