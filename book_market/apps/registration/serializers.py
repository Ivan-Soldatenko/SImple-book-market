from django.contrib.auth.models import User
from rest_framework import serializers

from apps.registration.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model"""

    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="username")

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "user",
            "is_valid",
            "information",
            "date_joined",
        )


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "is_active",
            "profile",
        )
