from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Teacher, Student, Remarks
from .forms import TeacherForm, StudentForm

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
        teacher = form.save()

        messages.add_message(request, messages.SUCCESS, "New teacher added")

        return redirect("class:teacher-view", teacher_id=teacher.id)

def teachersList(request):
    teachers = Teacher.objects.all()
    
    return render(request, "teachersList.html", {
        "teachers": teachers
    })

def studentsList(request):
    students = Student.objects.all()

    return render(request, "studentsList.html", {
        "students": students
    })

def addStudentToTeacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    student = Student.objects.get(pk=request.POST.get("student"))
    fav = "True" if request.POST.get("fav") else "False"

    teacher.students.add(student, through_defaults={"favorite":fav})

    messages.add_message(request, messages.SUCCESS, "New student added to the teacher")

    return redirect("class:teacher-view", teacher_id=teacher_id)

def updateFavorite(request, teacher_id, student_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    student = Student.objects.get(pk=student_id)
    fav = "True" if request.POST.get("fav-student") else "False"
    Remarks.objects.filter(teacher=teacher, student=student).update(favorite=fav)

    messages.add_message(request, messages.SUCCESS, "Favorites has been updated")

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
    def post(self, request, teacher_id):
        teacher = Teacher.objects.get(pk=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        form.save()

        messages.add_message(request, messages.SUCCESS, "Teacher %s has been updated" % teacher.name)

        return redirect("class:teacher-view", teacher_id=teacher_id)


class NewStudent(View):
    def get(self, request):
        form = StudentForm()

        return render(request, "addStudent.html", {
            "form": form
        })

    def post(self, request):
        form = StudentForm(request.POST)
        student = form.save()

        messages.add_message(request, messages.SUCCESS, "New student created")

        return redirect("class:student-view", student_id=student.id)


class StudentView(View):
    def get(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        form = StudentForm(instance=student)

        return render(request, "manageStudent.html", {
            "form": form, "student": student
        })

    def post(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)

        messages.add_message(request, messages.SUCCESS, "Student %s has been updated" % student.name)

        return redirect("class:student-view", student_id=student_id)


def deleteAction(request, userType, id):
    if userType == "student":
        student = Student.objects.get(pk=id)
        for teacher in student.teacher_set.all():
            teacher.students.remove(student)
        messages.add_message(request, messages.SUCCESS, "Student %s has been deleted" % student.name)
        student.delete()        
        return redirect("class:students-list")
    if userType == "teacher":
        teacher = Teacher.objects.get(pk=id)
        for student in teacher.students.all():
            student.teacher_set.remove(teacher)
        messages.add_message(request, messages.SUCCESS, "Teacher %s has been deleted" % teacher.name)
        teacher.delete()
        return redirect("class:teachers-list")
