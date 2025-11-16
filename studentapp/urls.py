from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_view, name="home"),
    # path("", home_view, name="home"),
    path("insert-students/", insert_students, name="insert-students"),
    path("display-all/", display_students, name="display-students"),
    path("update-student/<int:roll>/", update_student_view, name="update-students"),
    path("delete-student/<int:roll>/", delete_student_view, name="delete-student"),
]