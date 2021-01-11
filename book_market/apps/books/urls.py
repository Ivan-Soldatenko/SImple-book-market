"""Defines URL patterns for books app"""

from rest_framework.routers import DefaultRouter

from apps.books import views as books_views
from apps.registration import views as reg_views

app_name = "books"
router = DefaultRouter()
router.register("books", books_views.BookViewSet, basename="book")
router.register("authors", books_views.AuthorViewSet, basename="author")
router.register("genres", books_views.GenreViewSet, basename="genre")
router.register("users", reg_views.UserViewSet, basename="user")
router.register("userprofiles", reg_views.UserProfileViewSet, basename="userprofile")

urlpatterns = router.urls
