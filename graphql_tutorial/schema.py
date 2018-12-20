import graphene
import graphql_jwt

import links.schema
import links.schema_relay
from .users.schema import UserQuery, UserMutaion

class Query(
  UserQuery,
  links.schema.Query,
  links.schema_relay.RelayQuery,
  graphene.ObjectType):
  pass

class Mutation(UserMutaion, links.schema.Mutation, graphene.ObjectType):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_toekn = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
