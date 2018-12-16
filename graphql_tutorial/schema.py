import graphene

import links.schema
from .users.schema import UserQuery, UserMutaion

class Query(UserQuery, links.schema.Query, graphene.ObjectType):
  pass

class Mutation(UserMutaion, links.schema.Mutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
