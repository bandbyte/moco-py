"""Pydantic models for the Purchase Drafts resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class PurchaseDraftUser(BaseModel):
    """A user embedded in a purchase draft."""

    id: int
    firstname: str
    lastname: str


class PurchaseDraft(BaseModel):
    """A purchase draft in MOCO."""

    id: int
    title: str | None = None
    email_from: str | None = None
    email_body: str | None = None
    user: PurchaseDraftUser | None = None
    file_url: str | None = None
    created_at: datetime
    updated_at: datetime
