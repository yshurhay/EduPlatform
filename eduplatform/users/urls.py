from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from .endpoints import (
    CustomUserViewSetAPI,
    StudentViewSetAPI,
    TeacherStudentListAPIView,
    TeacherViewSetAPI,
)

router = SimpleRouter()
router.register("customusers", CustomUserViewSetAPI)
router.register("students", StudentViewSetAPI)
router.register("teachers", TeacherViewSetAPI)


urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "group/(?P<pk>[^/.]+)/teachers-students/", TeacherStudentListAPIView.as_view()
    ),
]
