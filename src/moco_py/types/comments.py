"""Pydantic models for the Comments resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedUserRef as EmbeddedUser
from ._enums import CommentableType


class Comment(BaseModel):
    """A comment (note) in MOCO."""

    id: int
    commentable_id: int
    commentable_type: CommentableType
    text: str
    manual: bool
    user: EmbeddedUser
    created_at: datetime.datetime
    updated_at: datetime.datetime
