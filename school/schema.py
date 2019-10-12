import graphene
import classroom.schema

class Query(
    classroom.schema.Query,
    graphene.ObjectType):
    pass

# class Mutation(classroom.schema.Mutation, graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query)