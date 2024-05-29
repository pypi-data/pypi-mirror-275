from typing import List
from typing import Optional

from pydantic import AnyUrl
from pydantic import Field

from ..base import SCIM2Model
from .resource import Resource


class SchemaExtension(SCIM2Model):
    schema_: AnyUrl = Field(..., alias="schema")
    """The URI of a schema extension."""

    required: bool
    """A Boolean value that specifies whether or not the schema extension is
    required for the resource type.

    If true, a resource of this type MUST include this schema extension
    and also include any attributes declared as required in this schema
    extension. If false, a resource of this type MAY omit this schema
    extension.
    """


class ResourceType(Resource):
    schemas: List[str] = ["urn:ietf:params:scim:schemas:core:2.0:ResourceType"]

    id: Optional[str] = None
    """The resource type's server unique id.

    May be the same as the 'name' attribute.
    """

    name: str
    """The resource type name.

    When applicable, service providers MUST specify the name, e.g.,
    'User'.
    """

    description: Optional[str] = None
    """The resource type's human-readable description.

    When applicable, service providers MUST specify the description.
    """

    endpoint: str
    """The resource type's HTTP-addressable endpoint relative to the Base URL,
    e.g., '/Users'."""

    schema_: AnyUrl = Field(..., alias="schema")
    """The resource type's primary/base schema URI."""

    schema_extensions: Optional[List[SchemaExtension]] = None
    """A list of URIs of the resource type's schema extensions."""
