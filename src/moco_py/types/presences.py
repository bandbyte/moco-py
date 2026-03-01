"""Pydantic models for the User Presences resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel, Field

from ._embedded import EmbeddedUserRef as EmbeddedUser


class Presence(BaseModel):
    """A user presence (work time entry) in MOCO."""

    model_config = {"populate_by_name": True}

    id: int
    date: datetime.date
    from_time: datetime.time | None = Field(None, alias="from")
    to: datetime.time | None = None
    is_home_office: bool | None = None
    user: EmbeddedUser
    created_at: datetime.datetime
    updated_at: datetime.datetime
