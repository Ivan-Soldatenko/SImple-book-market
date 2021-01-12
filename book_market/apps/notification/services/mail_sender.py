from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from apps.notification.models import BookAddedNotification


def send_book_addition_notification(title: str):
    """Send book addition notification to all users, who was followed notification"""

    for notification in BookAddedNotification.objects.all():
        _send_mail_message(
            template="notification/book_addition_notification.html",
            mail_subject="New book!",
            username=notification.username,
            user_email=notification.email,
            title=title,
        )


def _send_mail_message(
    template: str, mail_subject: str, username: str, user_email: str, title: str
) -> None:
    """Send mail message to users"""

    message = render_to_string(
        template, {"username": username, "domain": "0.0.0.0:8000", "title": title}
    )

    email = EmailMessage(mail_subject, message, to=[user_email])
    email.send()
