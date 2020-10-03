from django.db import models


class Book(models.Model):
	"""
	The book the user wants to know about
	"""

	title = models.CharField(max_length=50)
	author_name = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		"""
		return a string representation of the book's model
		"""

		return self.title
