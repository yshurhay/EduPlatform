from rest_framework.viewsets import ModelViewSet
from .models import (Specialization,
                     Course,
                     Group,
                     Topic,
                     Test,
                     Question,
                     Answer,
                     Article,
                     CompletedTest)

from .serializers import (SpecializationSerializer,
                            CourseSerializer,
                            GroupSerializer,
                            TopicSerializer,
                            TestSerializer,
                            QuestionSerializer,
                            AnswerSerializer,
                            ArticleSerializer,
                            CompletedTestSerializer)






class SpecializationViewsetAPI(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class CourseViewsetAPI(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewsetAPI(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TopicViewsetAPI(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TestViewsetAPI(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewsetAPI(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewsetAPI(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer



class ArticleViewsetAPI(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CompletedTestViewsetAPI(ModelViewSet):
    queryset = CompletedTest.objects.all()
    serializer_class = CompletedTestSerializer














