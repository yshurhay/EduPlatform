from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.views import (
    signup_view,
    verify_email,
    verify_email_complete,
    verify_email_confirm,
    verify_email_done,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("coursesapi/", include("courses.urls")),
    path("usersapi/", include("users.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("signup/", signup_view, name="signup"),
    path("verify-email/", verify_email, name="verify-email"),
    path("verify-email/done/", verify_email_done, name="verify-email-done"),
    path(
        "verify-email-confirm/<uidb64>/<token>/",
        verify_email_confirm,
        name="verify-email-confirm",
    ),
    path("verify-email/complete/", verify_email_complete, name="verify-email-complete"),
]
