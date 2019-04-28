from typing import Optional

from email_validator import validate_email
import graphene
from graphene.types import Scalar
from graphql.language import ast


class Email(Scalar):
    """An email address as defined by RFC 822"""

    @staticmethod
    def serialize(email: str) -> str:
        return email

    @staticmethod
    def parse_literal(node: graphene.Node) -> Optional[str]:
        if isinstance(node, ast.StringValue):
            return validate_email(node.value)["email"]
        else:
            return None

    @staticmethod
    def parse_value(value: str) -> str:
        return validate_email(value)["email"]
