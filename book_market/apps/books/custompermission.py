from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """Permission class"""

    def has_permission(self, request, view):
        """
        Only admins can create and update instances. Other users can view list of
        instances or detail information about the certain instance
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
