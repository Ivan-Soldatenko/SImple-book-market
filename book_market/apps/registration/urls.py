from rest_framework.routers import DefaultRouter

from apps.registration import views

router = DefaultRouter()
router.register("signup", views.SignUpView, basename="signup")

urlpatterns = router.urls
