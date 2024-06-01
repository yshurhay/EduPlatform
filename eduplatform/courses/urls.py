from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .endpoints import (SpecializationViewsetAPI,
                        CourseViewsetAPI,
                        GroupViewsetAPI,
                        TopicViewsetAPI,
                        TestViewsetAPI,
                        QuestionViewsetAPI,
                        AnswerViewsetAPI,
                        ArticleViewsetAPI,
                        CompletedTestViewsetAPI,
                        ImageViewSetAPI)


router = SimpleRouter()
router.register('specializations', SpecializationViewsetAPI)
router.register('courses', CourseViewsetAPI)
router.register('groups', GroupViewsetAPI)
router.register('topics', TopicViewsetAPI)
router.register('tests', TestViewsetAPI)
router.register('questions', QuestionViewsetAPI)
router.register('answers', AnswerViewsetAPI)
router.register('articles', ArticleViewsetAPI)
router.register('completedtests', CompletedTestViewsetAPI)
router.register('images', ImageViewSetAPI)



urlpatterns = [
    path('', include(router.urls)),
]