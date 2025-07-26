from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import UserProfile

# Function-based view
def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books}) 
# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  
    context_object_name = "library"  
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
def role_check(role):
    def check(user):
        try:
            return user.userprofile.role == role
        except UserProfile.DoesNotExist:
            return False
    return user_passes_test(check)

@login_required
@role_check("Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
@role_check("Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
@role_check("Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")