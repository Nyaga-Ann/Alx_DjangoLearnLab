
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Book
from .forms import BookSearchForm
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/view.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('view_articles')
    return render(request, 'articles/create.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('view_articles')
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('view_articles')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)  # SAFE ORM query
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
