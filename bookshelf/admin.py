from django.contrib import admin
from .models import Book

# Custom admin class for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Show these columns in admin list
    list_filter = ('author', 'published_date')            # Add sidebar filters
    search_fields = ('title', 'author')                   # Enable search box

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)

