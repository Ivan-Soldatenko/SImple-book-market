from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.notification.serializers import BookAddedNotificationSerializer


class NotificationAdditionBookViewSet(viewsets.GenericViewSet):
    """View for register notification for users"""

    serializer_class = BookAddedNotificationSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        """Function returns information about view"""

        data = {"information": "Click on the button below to confirm mail notification"}
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """Function confirm user's notification"""

        serializer = self.get_serializer(
            data={"email": request.user.email, "username": request.user.username}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = {
            "information": "You have successfully followed to book's addition mail notification"
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """Function create user's notification"""

        serializer.save()
