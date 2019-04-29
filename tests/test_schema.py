import graphene

from reader_server.graphql.query import Query


def test_schema_loads() -> None:
    schema = graphene.Schema(query=Query)
    assert schema is not None
