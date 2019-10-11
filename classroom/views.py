from django.shortcuts import render, redirect
from django.views import View
from .models import Teacher, Student, Remarks
from .forms import TeacherForm

def Home(request):
    return render(request, "index.html", {})

class NewTeacher(View):
    def get(self, request):
        form = TeacherForm()

        return render(request, "addTeacher.html", {
            "form": form
        })
    
    def post(self, request):
        form = TeacherForm(request.POST)
        form.save()

        return redirect("class:index")

def teachersList(request):
    teachers = Teacher.objects.all()
    
    return render(request, "teachersList.html", {
        "teachers": teachers
    })

def addStudentToTeacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    student = Student.objects.get(pk=request.POST.get("student"))
    fav = True if request.POST.get("fav") else False

    teacher.students.add(student, through_defaults={"favorite":fav})

    return redirect("class:teacher-view", teacher_id=teacher_id)

def updateFavorite(request, teacher_id, student_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    student = Student.objects.get(pk=student_id)
    fav = True if request.POST.get("fav-student") else False
    Remarks.objects.filter(teacher=teacher, student=student).update(favorite=fav)

    return redirect("class:teacher-view", teacher_id=teacher_id)

class TeacherView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(pk=teacher_id)
        form = TeacherForm(instance=teacher)
        students = Student.objects.exclude(teacher=teacher)
        remarks = Remarks.objects.filter(teacher=teacher)

        return render(request, "manageTeacher.html", {
            "teacher": teacher, "form": form, "students": students, "remarks": remarks
        })