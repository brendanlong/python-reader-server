import graphene

import reader_server.query


def test_schema_loads() -> None:
    schema = graphene.Schema(query=reader_server.query.Query)
    assert schema is not None
