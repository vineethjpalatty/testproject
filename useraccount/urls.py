from rest_framework.routers import DefaultRouter

from useraccount.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users'),
urlpatterns = router.urls