from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    """Class for result's pagination"""

    # Set maximum limit value to 8
    max_limit = 8
