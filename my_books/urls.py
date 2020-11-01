"""Defines URL patterns for my_books app"""

from django.urls import path
from rest_framework.routers import SimpleRouter
from my_books import views

app_name = "my_books"
router = SimpleRouter()
router.register('books', views.BooksView)

urlpatterns = router.urls