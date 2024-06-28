from django.urls import path, include
from rest_framework import routers
from .views import WaterBucketViewSet

router = routers.DefaultRouter()
router.register(r"water-bucket", WaterBucketViewSet, basename="water-bucket")

urlpatterns = [
    path("", include(router.urls)),
]
