from celery import Celery


app = Celery("book_market")
app.autodiscover_tasks()
