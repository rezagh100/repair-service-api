from django.urls import path
from .views import RepairRequestListAPIView

urlpatterns = [
    path(
        "",
        RepairRequestListAPIView.as_view(),
        name="repair-list"
    ),
]