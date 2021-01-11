from apps.books.models import Author, Book, Genre
from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Class for addition Author model to admin panel"""

    list_display = ("first_name", "last_name",)
    list_filter = ("country",)
    search_fields = ("first_name", "last_name", "country", "born_year",)
    ordering = ("first_name", "last_name", "born_year",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Class for addition Genre model to admin panel"""

    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Class for addition Book model to admin panel"""

    list_display = ("title", "genre", "author",)
    list_filter = ("title", "genre__name", "author__first_name", "author__last_name", "publish_date",)
    search_fields = ("title", "genre__name", "author__first_name", "author__last_name",)
    ordering = ("title", "genre__name", "author__name", "publish_date",)
