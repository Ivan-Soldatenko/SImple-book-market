from apps.books.models import Author, Book, Genre
from rest_framework import serializers


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
    """
	Serializer for representing books with short information
	"""

    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "publish_date", "description")


class BookPostSerializer(serializers.ModelSerializer):
    """
	Serializer for representing books with full information
	"""

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "publish_date", "description")
