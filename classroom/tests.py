from django.test import TestCase
from .models import Teacher, Student, Remarks

class Classroom(TestCase):  
    # creating objects for testing  
    def setUp(self):
        Teacher.objects.create(name="Amit Shah", subject="Maths")
        Teacher.objects.create(name="Narendra Modi", subject="Physics")
        Student.objects.create(name="Rahul Gandhi", age=45)
        Student.objects.create(name="Mamta Banerjee", age=60)            

    # checking if student has teachers
    def test_has_teachers(self):        
        rahul = Student.objects.get(name="Rahul Gandhi")
        mamta = Student.objects.get(name="Mamta Banerjee")
        modi = Teacher.objects.get(name="Narendra Modi")
        amit = Teacher.objects.get(name="Amit Shah")

        modi.students.add(rahul)
        amit.students.add(mamta)

        self.assertTrue(rahul.teacher_set.all, "Rahul has teachers")
        self.assertTrue(mamta.teacher_set.all, "Mamta has teachers")

    # checking if student is favorite or not test case. one test case will return false
    def test_student_is_favorite(self):
        rahul = Student.objects.get(name="Rahul Gandhi")
        modi = Teacher.objects.get(name="Narendra Modi")

        modi.students.add(rahul, through_defaults={"favorite":True})
        remark = Remarks.objects.get(student=rahul)

        self.assertTrue(remark.favorite, "The student is favorite")
        self.assertFalse(remark.favorite, "Yes, the student is favorite") #This is supposed to fail. Worrysome if it doesn't fail.
