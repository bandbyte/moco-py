"""Pydantic models for the Tags resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class Tag(BaseModel):
    """A tag (label) in MOCO."""

    id: int
    name: str
    color: str | None = None
    context: str
    created_at: datetime
    updated_at: datetime
