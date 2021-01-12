from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.notification.models import BookAddedNotification


class BookAddedNotificationSerializer(serializers.ModelSerializer):
    """Serializer for BookAddedNotification model"""

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=BookAddedNotification.objects.all())]
    )
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=BookAddedNotification.objects.all())]
    )

    class Meta:
        model = BookAddedNotification
        fields = ("username", "email",)
        read_only_fields = ("username", "email",)
