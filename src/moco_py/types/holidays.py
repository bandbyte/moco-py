"""Pydantic models for the User Holidays resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedUserRef as EmbeddedUser


class Holiday(BaseModel):
    """A user holiday entitlement in MOCO."""

    id: int
    year: int
    title: str
    days: int
    hours: float
    user: EmbeddedUser
    creator: EmbeddedUser | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
