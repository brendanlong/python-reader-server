#!/usr/bin/env python3
import asyncio

import graphene
from graphql.execution.executors.asyncio import AsyncioExecutor

from reader_server.backends.memory import Db
from reader_server.graphql.context import Context
from reader_server.graphql.query import Query


async def main() -> None:
    loop = asyncio.get_event_loop()
    executor = AsyncioExecutor(loop=loop)
    schema = graphene.Schema(query=Query)
    print(schema)
    result = await schema.execute(
        "{ users { edges { node { id } } } }",
        context=Context(Db()),
        executor=executor,
        return_promise=True)
    if result.errors:
        print(result.errors)
    else:
        print(result.data)


if __name__ == "__main__":
    asyncio.run(main())
