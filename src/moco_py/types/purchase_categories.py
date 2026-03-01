"""Pydantic models for the Purchase Categories resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class PurchaseCategory(BaseModel):
    """A purchase category in MOCO."""

    id: int
    name: str
    credit_account: str | None = None
    active: bool
    created_at: datetime
    updated_at: datetime
