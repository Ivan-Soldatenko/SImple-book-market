from apps.books.models import Author, Book, Genre
from apps.books.serializers import (AuthorSerializer, BookPostSerializer,
                                    BookSerializer, GenreSerializer)
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for Book model"""

    queryset = Book.objects.all()

    filter_fields = ("title",)
    search_fields = ("title",)
    ordering_fields = ("title",)

    def get_serializer_class(self):
        """
        Function return serializer class
        If action is create or update function returns BookPostSerializer
        In other cases returns BookSerializer
        """

        if self.action == "create" or self.action == "update":
            return BookPostSerializer

        return BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for Author model"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for Genre model"""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
