from rest_framework import serializers

from my_books.models import Book


class ShortBookSerializer(serializers.ModelSerializer):
	"""
	Serializer for representing books with short information
	"""
	
	class Meta:
		model = Book
		exclude = ['description']


class FullBookSerializer(serializers.ModelSerializer): 
	"""
	Serializer for representing books with full information
	"""

	class Meta:
		model = Book
		fields = ['id', 'title', 'author_name', 'description']