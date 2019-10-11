from django import forms
from .models import Teacher, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subject"]