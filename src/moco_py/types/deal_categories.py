"""Pydantic models for the Deal Categories resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class DealCategory(BaseModel):
    """A deal category (Akquise-Stufe) in MOCO."""

    id: int
    name: str
    probability: int
    created_at: datetime
    updated_at: datetime
