import asyncio

import graphene
from graphql.execution.executors.asyncio import AsyncioExecutor

import reader_server.query


async def main() -> None:
    loop = asyncio.get_event_loop()
    executor = AsyncioExecutor(loop=loop)
    schema = graphene.Schema(query=reader_server.query.Query)
    print(schema)
    result = await schema.execute(
        "{ users { id } }",
        executor=executor,
        return_promise=True)
    print(result.data)


if __name__ == "__main__":
    asyncio.run(main())
