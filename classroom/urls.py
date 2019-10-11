from django.urls import path
from . import views

app_name = "class"

urlpatterns = [
    path('', views.Home, name="index"),
    path('add-teacher', views.NewTeacher.as_view(), name="add-teacher"),
    path('teachers-list', views.teachersList, name="teachers-list"),
    path('teacher/<int:teacher_id>', views.TeacherView.as_view(), name="teacher-view"),
    path('teacher/<int:teacher_id>/add-student', views.addStudentToTeacher, name="add-student-teacher"),
    path('teacher/<int:teacher_id>/update-fav/<int:student_id>', views.updateFavorite, name="update-teacher-favorite"),
    path('add-student', views.NewStudent.as_view(), name="add-student"),
]