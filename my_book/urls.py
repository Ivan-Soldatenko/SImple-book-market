from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # url for api
    path('api/v1/', include('my_books.urls')),
    # url for authentication system
    path('api-auth/', include('rest_framework.urls')),
]
