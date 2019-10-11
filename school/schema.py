import graphene
import classroom.schema

class Query(
    classroom.schema.Query,
    graphene.ObjectType):

    pass

schema = graphene.Schema(query=Query)