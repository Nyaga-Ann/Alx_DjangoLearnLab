\# CREATE

>>> book = Book(title="1984", author="George Orwell", published\_date="1949-01-01")

>>> book.save()

\# Output: Book object created successfully



\# RETRIEVE

>>> Book.objects.get(title="1984")

\# Output: <Book: 1984>, author=George Orwell, published\_date=1949-01-01



\# UPDATE

>>> book = Book.objects.get(title="1984")

>>> book.title = "Nineteen Eighty-Four"

>>> book.save()

\# Output: Book title updated



\# DELETE

>>> book.delete()

\# Output: (1, {'bookshelf.Book': 1})



