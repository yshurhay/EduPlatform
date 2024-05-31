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
                        CompletedTestViewsetAPI)


router = SimpleRouter()
router.register('specialization', SpecializationViewsetAPI)
router.register('course', CourseViewsetAPI)
router.register('group', GroupViewsetAPI)
router.register('topic', TopicViewsetAPI)
router.register('test', TestViewsetAPI)
router.register('question', QuestionViewsetAPI)
router.register('answer', AnswerViewsetAPI)
router.register('article', ArticleViewsetAPI)
router.register('completedtest', CompletedTestViewsetAPI)



urlpatterns = [
    path('', include(router.urls)),
]