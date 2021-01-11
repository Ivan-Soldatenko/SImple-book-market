from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

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


class SignUpView(viewsets.GenericViewSet):
    """View for registration on the API for users"""

    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        """Function for represent information about view for users"""

        data = {
            "information": "You need to fill fields below with the correct information"
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Function create new user instance"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = {
            "information": "You are successfully registered on the book-market API"
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """Function works when user send correct information"""

        serializer.save()
