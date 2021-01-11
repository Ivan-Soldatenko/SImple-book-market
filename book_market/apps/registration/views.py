from rest_framework import viewsets
from django.contrib.auth.models import User

from apps.registration.models import UserProfile
from apps.registration.serializers import UserSerializer, UserProfileSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for User model"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for UserProfile model"""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
