from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterAPIView,
    MeAPIView,
    ChangePasswordAPIView,
)
from .views import RegisterAPIView, MeAPIView
from .views import RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("me/", MeAPIView.as_view()),
    path(
    "change-password/",
    ChangePasswordAPIView.as_view(),
    name="change-password",
),
]