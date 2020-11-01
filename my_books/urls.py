"""Defines URL patterns for my_books app"""

from django.urls import path

from my_books.views import BooksView

app_name = 'my_books'
urlpatterns = [
	# Page for viewing all books with short information about their (without description)
	path('books/', BooksView.as_view({'get': 'list', 'post': 'create'})),
	# Page for viewing a book with full information about it (with descriprion)
	path('books/<int:pk>/', BooksView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]