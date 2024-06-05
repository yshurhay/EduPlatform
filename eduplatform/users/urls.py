from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .endpoints import CustomUserViewSetAPI, StudentViewSetAPI, TeacherViewSetAPI, TeacherStudentListAPIView

router = SimpleRouter()
router.register("customusers", CustomUserViewSetAPI)
router.register("students", StudentViewSetAPI)
router.register("teachers", TeacherViewSetAPI)


urlpatterns = [
    path("", include(router.urls)),
    path('group/<int:pk>/teachers-students/', TeacherStudentListAPIView.as_view())
]
