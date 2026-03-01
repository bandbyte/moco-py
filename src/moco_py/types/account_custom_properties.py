"""Pydantic models for the Account Custom Properties resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class CustomProperty(BaseModel):
    """A custom property in MOCO."""

    id: int
    name: str
    name_alt: str | None = None
    placeholder: str | None = None
    placeholder_alt: str | None = None
    entity: str
    kind: str
    print_on_invoice: bool | None = None
    print_on_offer: bool | None = None
    print_on_timesheet: bool | None = None
    notification_enabled: bool | None = None
    defaults: list[str] | None = None
    created_at: datetime
    updated_at: datetime
