"""Defines URL patterns for books app"""

from rest_framework.routers import DefaultRouter

from apps.books import views

app_name = "books"
router = DefaultRouter()
router.register("books", views.BookViewSet, basename="book")
router.register("authors", views.AuthorViewSet, basename="author")
router.register("genres", views.GenreViewSet, basename="genre")

urlpatterns = router.urls
