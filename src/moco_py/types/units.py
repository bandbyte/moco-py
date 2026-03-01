"""Pydantic models for the Units (Teams) resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedUserRef


class EmbeddedUser(EmbeddedUserRef):
    """A user embedded in a unit response (includes email)."""

    email: str


class Unit(BaseModel):
    """A unit (team) in MOCO."""

    id: int
    name: str
    users: list[EmbeddedUser]
    created_at: datetime
    updated_at: datetime
