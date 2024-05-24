from typing import List
from typing import Optional
from typing import Tuple

from pydantic import BaseModel
from pydantic import Field


class GroupMember(BaseModel):
    value: Optional[str] = None
    display: Optional[str] = None


class Group(BaseModel):
    id: Optional[str] = None
    displayName: str = Field(
        ..., description="A human-readable name for the Group. REQUIRED."
    )
    members: Optional[List[GroupMember]] = Field(
        None, description="A list of members of the Group."
    )
    schemas: Tuple[str] = ("urn:ietf:params:scim:schemas:core:2.0:Group",)
