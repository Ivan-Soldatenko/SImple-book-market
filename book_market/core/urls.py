from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # url for api
    path("api/v1/", include("apps.books.urls")),
    # url for authentication system
    path("api-auth/", include("rest_framework.urls")),
]
