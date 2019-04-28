#!/usr/bin/env python3
import asyncio
import json

import graphene
from graphql.execution.executors.asyncio import AsyncioExecutor

from reader_server.backends.memory import Db
from reader_server.graphql.context import Context
from reader_server.graphql.mutations import Mutations
from reader_server.graphql.query import Query


async def main() -> None:
    loop = asyncio.get_event_loop()
    executor = AsyncioExecutor(loop=loop)
    schema = graphene.Schema(query=Query, mutation=Mutations)
    context = Context(Db())
    print(schema)

    print("Creating users")
    for email in ["brendan@example.com", "test@example.com"]:
        result = await schema.execute(
            """
            mutation createUser($email: Email!) {
                createUser(email: $email, password:"test") {
                    user {
                        id, email
                    }
                }
            }
            """,
            context=context,
            executor=executor,
            variables={"email": email},
            return_promise=True)
        if result.errors:
            print(result.errors)
        else:
            print(json.dumps(result.data, indent=2))
            user_id = result.data["createUser"]["user"]["id"]

    print("Getting users")
    result = await schema.execute(
        """
        { users(first: 1) { edges { cursor, node { email } }, pageInfo { hasNextPage } } }
        """,
        context=context,
        executor=executor,
        return_promise=True)
    if result.errors:
        print(result.errors)
    else:
        print(json.dumps(result.data, indent=2))

    print("Getting user by ID")
    result = await schema.execute(
        """
        { node(id:"%s"){ id } }
        """ % user_id,
        context=context,
        executor=executor,
        return_promise=True)
    if result.errors:
        print(result.errors)
    else:
        print(json.dumps(result.data, indent=2))

    print("Get current user")
    context = Context(context.db, (await context.db.users.all())[0])
    result = await schema.execute(
        """
        { user{ id } }
        """,
        context=context,
        executor=executor,
        return_promise=True)
    if result.errors:
        print(result.errors)
    else:
        print(json.dumps(result.data, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
