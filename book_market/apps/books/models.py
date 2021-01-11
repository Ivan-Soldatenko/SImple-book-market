from django.db import models


class Author(models.Model):
    """Represent author instance"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    born_year = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('first_name', 'last_name',)
        ordering = ('last_name', 'first_name',)

    def __str__(self):
        """Return string representation of author's model"""

        return f"{self.last_name} {self.first_name}"


class Book(models.Model):
    """Represent book instance"""

    title = models.CharField(max_length=50, blank=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='book', related_query_name='book')
    description = models.TextField(blank=False)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        """Return a string representation of the book's model"""

        return self.title
