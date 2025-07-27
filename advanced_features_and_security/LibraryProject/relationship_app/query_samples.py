import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)).replace("\\relationship_app", ""))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name}:")
    for book in books:
        print(f"- {book.title}")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")

# Example usage (uncomment to test after populating DB)
books_by_author("Jane Austen")
books_in_library("Central Library")
librarian_for_library("Central Library")
