from django.db import models


class BookAddedNotification(models.Model):
    """
    Model for storing users, who followed to notification in book-market API
    Notification will be sent when new books appear in the book-market
    """

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        """Return string representation about user's notification"""

        return self.email
