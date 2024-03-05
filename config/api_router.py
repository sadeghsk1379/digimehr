from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from core.api.views import AllUserViewSet, NewUserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()  # type: ignore

router.register("newusers", NewUserViewSet, basename="newusers")
router.register("allusers", AllUserViewSet, basename="alluser")


# router.register("categories", CategoryViewset, basename="category")


app_name = "api"
urlpatterns = router.urls
