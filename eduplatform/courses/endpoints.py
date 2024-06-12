from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from users.models import Student, Teacher
from users.serializers import StudentSerializer, TeacherSerializer

from .models import (
    Answer,
    Article,
    CompletedTest,
    Course,
    Group,
    Image,
    Question,
    Specialization,
    Test,
    Topic,
)
from .serializers import (
    AnswerSerializer,
    ArticleSerializer,
    CompletedTestSerializer,
    CourseSerializer,
    GroupSerializer,
    ImageSerializer,
    QuestionSerializer,
    SpecializationSerializer,
    TestSerializer,
    TopicSerializer,
)


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


class ImageViewSetAPI(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class StudentCoursesListAPIView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        student = Student.objects.get(pk=pk)
        groups = student.group_set.all()
        return [group.course for group in groups]


class GroupStudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        group = Group.objects.get(pk=pk)
        return Student.objects.filter(group=group).all()


class TeacherRecommendationListAPIView(ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        course = Course.objects.get(pk=pk)
        course_specialization = course.specialization.all()
        rec_teachers = Teacher.objects.filter(course_specialization_in=course_specialization).distinct()
        return rec_teachers
