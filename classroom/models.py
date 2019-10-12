from django.db import models

SUBJECTS = (
    ("Maths", "Maths"),
    ("Chemistry", "Chemistry"),
    ("Physics", "Physics")
)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, choices=SUBJECTS)
    students = models.ManyToManyField(Student, through="Remarks")

    def __str__(self):
        return self.name

# Table to hold the favorite remark
class Remarks(models.Model):
    student = models.ForeignKey(Student, related_name="student", on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, related_name="teacher", on_delete=models.DO_NOTHING)
    favorite = models.CharField(default="False", max_length=10, choices=(
        ("True", "Yes"),
        ("False", "No")
    ))

