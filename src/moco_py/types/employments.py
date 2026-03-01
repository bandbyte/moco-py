"""Pydantic models for the User Employments resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel, Field

from ._embedded import EmbeddedUserRef as EmbeddedUser


class EmploymentPattern(BaseModel):
    """Work hour pattern for morning and afternoon."""

    am: list[float]
    pm: list[float]


class Employment(BaseModel):
    """A user employment (weekly work model) in MOCO."""

    model_config = {"populate_by_name": True}

    id: int
    weekly_target_hours: float
    pattern: EmploymentPattern
    from_date: datetime.date | None = Field(None, alias="from")
    to: datetime.date | None = None
    user: EmbeddedUser
    created_at: datetime.datetime
    updated_at: datetime.datetime
