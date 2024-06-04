from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('coursesapi/', include('courses.urls')),
    path('usersapi/', include('users.urls'))
]
