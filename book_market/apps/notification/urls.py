from rest_framework.routers import DefaultRouter

from apps.notification import views


router = DefaultRouter()
router.register(
    "addition_book", views.NotificationAdditionBookViewSet, basename="addition_book"
)

urlpatterns = router.urls
