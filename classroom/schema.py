import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Teacher, Student, Remarks

class RemarkNode(DjangoObjectType):
    class Meta:
        model = Remarks
        filter_fields = ['favorite']
        interfaces = (relay.Node, )


class TeacherNode(DjangoObjectType):
    favorite = graphene.Field(RemarkNode)

    class Meta:
        model = Teacher
        filter_fields = ['name', 'subject']
        interfaces = (relay.Node, )


class StudentNode(DjangoObjectType):
    class Meta:
        model = Student
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'age': ['exact'],            
            'favorite': ['exact']
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    teacher = relay.Node.Field(TeacherNode)
    all_teachers = DjangoFilterConnectionField(TeacherNode)

    student = relay.Node.Field(StudentNode)
    all_students = DjangoFilterConnectionField(StudentNode)

    def resolve_favorites(self, info, **kwargs):
        teacher = Teacher.objects.get(pk=self.id)
        remarks = Remarks.objects.filter(teacher=teacher)
        return [each.student for each in remarks]