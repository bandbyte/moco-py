"""Pydantic models for the User Work Time Adjustments resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedUserRef as EmbeddedUser


class WorkTimeAdjustment(BaseModel):
    """A user work time adjustment in MOCO."""

    id: int
    date: datetime.date
    description: str
    hours: float
    creator: EmbeddedUser | None = None
    user: EmbeddedUser
    created_at: datetime.datetime
    updated_at: datetime.datetime
