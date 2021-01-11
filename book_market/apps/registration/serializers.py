from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from apps.registration.models import UserProfile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model"""

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        model = UserProfile
        fields = ("id", "user", "is_valid", "information", "date_joined")


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    profile = UserProfileSerializer(read_only=True)

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "password2",
            "is_active",
            "profile",
        )
        read_only_fields = ("is_active",)

    def validate(self, attrs):
        """Check that received correct data from user"""

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        """Method for creating user instance"""

        user = User.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
