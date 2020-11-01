from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from my_books.models import Book
from my_books.serializers import ShortBookSerializer, FullBookSerializer


class BooksView(viewsets.mixins.ListModelMixin,
				viewsets.mixins.CreateModelMixin,
				viewsets.mixins.RetrieveModelMixin,
				viewsets.mixins.UpdateModelMixin,
				viewsets.mixins.DestroyModelMixin,
				viewsets.GenericViewSet):
	"""
	List all books with short information about their.
	Create a new book's model and retrieve a book with full information about it.
	"""

	queryset = Book.objects.all()

	def get_serializer_class(self):
		"""
		Override method for selecting correct serializer:
		list all books - ShortBookSerializer
		in other cases - FullBookSerializer
		"""

		if hasattr(self, 'action') and self.action == 'list':
			return ShortBookSerializer

		return FullBookSerializer
	

