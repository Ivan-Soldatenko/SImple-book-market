from rest_framework import viewsets

from apps.books.customfilter import AuthorFilter, BookFilter
from apps.books.custompermission import IsAdminUserOrReadOnly
from apps.books.models import Author, Book, Genre
from apps.books.serializers import (AuthorSerializer, BookPostSerializer,
                                    BookSerializer, GenreSerializer)


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for Book model"""

    queryset = Book.objects.all()

    permission_classes = (IsAdminUserOrReadOnly,)

    filterset_class = BookFilter
    search_fields = ("title", "author__first_name", "author__last_name", "genre__name")
    ordering_fields = (
        "title",
        "author__first_name",
        "author__last_name",
        "genre__name",
        "publish_date",
    )

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

    permission_classes = (IsAdminUserOrReadOnly,)

    filterset_class = AuthorFilter
    search_fields = ("first_name", "last_name", "country")
    ordering_fields = ("first_name", "last_name", "born_date")


class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for Genre model"""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = (IsAdminUserOrReadOnly,)

    filterset_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)
