from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(self.client.login(username='testuser', password='testpass')
            title="Test Book",
            publication_year=2020,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.pk
        }
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        data = {
            'title': 'Updated Title',
            'publication_year': 2022,
            'author': self.author.pk
        }
        response = self.client.put('/books/update/{}/'.format(self.book.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete('/books/delete/{}/'.format(self.book.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        self.client.credentials()  # remove token
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_response = self.client.post('/books/create/', {
            'title': 'Fail Book',
            'publication_year': 2023,
            'author': self.author.pk
        })
        self.assertEqual(post_response.status_code, status.HTTP_401_UNAUTHORIZED)
