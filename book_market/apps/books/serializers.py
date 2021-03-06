from rest_framework import serializers

from apps.books.models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for author model"""

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "born_year", "country", "bio")


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for genre model"""

    class Meta:
        model = Genre
        fields = ("id", "name", "description")


class BookSerializer(serializers.ModelSerializer):
    """Serializer for representing book model. Using for GET request"""

    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "publish_date", "description")


class BookPostSerializer(serializers.ModelSerializer):
    """Serializer for representing book model. Using for POST and PUT request"""

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "publish_date", "description")
