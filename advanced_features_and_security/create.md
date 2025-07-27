\# Create Book Entry



```python

from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", published\_date="1949-01-01")

book.save()



