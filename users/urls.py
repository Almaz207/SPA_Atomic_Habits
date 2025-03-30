from rest_framework.permissions import AllowAny
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import (
    CustomUserCreateAPIView,
    CustomUserListAPIView,
    CustomUserRetrieveAPIView,
    CustomUserUpdateAPIView,
    CustomUserDestroyAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", CustomUserCreateAPIView.as_view(), name="register"),
    path("list_user/", CustomUserListAPIView.as_view(), name="list_user"),
    path(
        "user_retrieve/<int:pk>/",
        CustomUserRetrieveAPIView.as_view(),
        name="user_retrieve",
    ),
    path(
        "user_update/<int:pk>/", CustomUserUpdateAPIView.as_view(), name="user_update"
    ),
    path(
        "user_destroy/<int:pk>/",
        CustomUserDestroyAPIView.as_view(),
        name="user_destroy",
    ),
    path(
        "api/token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
