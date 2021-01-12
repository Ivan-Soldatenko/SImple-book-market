from rest_framework import serializers
from apps.notification.models import BookAddedNotification


class BookAddedNotificationSerializer(serializers.ModelSerializer):
    """Serializer for BookAddedNotification model"""

    class Meta:
        model = BookAddedNotification
        fields = ("username", "email")
