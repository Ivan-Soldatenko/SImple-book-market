from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Represent user's profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_valid = models.BooleanField(default=False)
    information = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Function create user's profile after creating new user's instance"""

    if created:
        UserProfile.objects.create(user=instance)
