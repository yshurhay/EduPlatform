from django.contrib import admin
from .models import (Specialization, Course, Group, Topic,
                     Test, Question, CompletedTest, Article, Answer)

admin.site.register(Specialization)
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Topic)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(CompletedTest)
admin.site.register(Article)
admin.site.register(Answer)
