from django_filters import DateTimeFilter, FilterSet

from apps.books.models import Author, Book


class AuthorFilter(FilterSet):
    """Filter class for Price model"""

    from_born_year = DateTimeFilter(field_name="born_year", lookup_expr="gte")
    to_born_year = DateTimeFilter(field_name="born_year", lookup_expr="lte")

    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "from_born_year",
            "born_year",
            "to_born_year",
        )


class BookFilter(FilterSet):
    """Filter class for Book model"""

    from_publish_date = DateTimeFilter(field_name="publish_date", lookup_expr="gte")
    to_publish_date = DateTimeFilter(field_name="publish_date", lookup_expr="lte")

    class Meta:
        model = Book
        fields = (
            "title",
            "author__first_name",
            "author__last_name",
            "genre__name",
            "from_publish_date",
            "publish_date",
            "to_publish_date",
        )
