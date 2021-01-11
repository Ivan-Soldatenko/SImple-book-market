"""Defines URL patterns for books app"""

from django.urls import path
from rest_framework.routers import SimpleRouter
from books import views

app_name = "books"
router = SimpleRouter()
router.register('books', views.BooksView)

urlpatterns = router.urls