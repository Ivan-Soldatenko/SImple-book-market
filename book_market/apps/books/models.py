from django.db import models


class Author(models.Model):
    """Represent author instance"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    born_year = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("first_name", "last_name")
        ordering = ("last_name", "first_name")

    def __str__(self):
        """Return string representation of author's model"""

        return f"{self.last_name} {self.first_name}"


class Genre(models.Model):
    """Represent genre instance"""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        """Return string representation of genre's model"""

        return self.name


class Book(models.Model):
    """Represent book instance"""

    title = models.CharField(max_length=50, unique=True)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name="book",
        related_query_name="book"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        related_name="book",
        related_query_name="book",
    )
    publish_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("-publish_date", "title")

    def __str__(self):
        """Return a string representation of the book's model"""

        return self.title
