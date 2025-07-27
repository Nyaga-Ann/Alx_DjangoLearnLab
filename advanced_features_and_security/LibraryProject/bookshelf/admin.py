from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Article

# Custom admin class for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Show these columns in admin list
    list_filter = ('author', 'published_date')            # Add sidebar filters
    search_fields = ('title', 'author')                   # Enable search box

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)