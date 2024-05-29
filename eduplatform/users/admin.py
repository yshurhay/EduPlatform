from django.contrib import admin

from .models import Teacher, Student, CustomUser

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Student)
