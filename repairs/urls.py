from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    RepairRequestViewSet,
)

router = DefaultRouter()

router.register(
    "categories",
    CategoryViewSet,
)

router.register(
    "requests",
    RepairRequestViewSet,
    basename="repair-request",
)

urlpatterns = [
    path("", include(router.urls)),
]