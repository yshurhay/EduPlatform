from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .endpoints import CustomUserViewSetAPI, StudentViewSetAPI, TeacherViewSetAPI


router = SimpleRouter()
router.register('customusers', CustomUserViewSetAPI)
router.register('students', StudentViewSetAPI)
router.register('teachers', TeacherViewSetAPI)


urlpatterns = [
    path('', include(router.urls))
]
