"""Pydantic models for the Profile resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ProfileUnit(BaseModel):
    """A unit embedded in a profile response."""

    id: int
    name: str


class Profile(BaseModel):
    """The current user's profile in MOCO."""

    id: int
    email: str
    full_name: str
    first_name: str
    last_name: str
    active: bool
    external: bool
    avatar_url: str | None = None
    unit: ProfileUnit | None = None
    created_at: datetime
    updated_at: datetime
