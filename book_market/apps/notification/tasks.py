from celery import shared_task

from apps.notification.services.mail_sender import send_book_addition_notification


@shared_task()
def book_addition_notification(title: str) -> None:
    """Function send notification about new book's addition to users"""

    send_book_addition_notification(title=title)
