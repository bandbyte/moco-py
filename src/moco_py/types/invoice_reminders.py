"""Pydantic models for the Invoice Reminders resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedInvoiceRef as EmbeddedInvoice


class InvoiceReminder(BaseModel):
    """An invoice reminder in MOCO."""

    id: int
    title: str | None = None
    text: str | None = None
    fee: float | None = None
    date: datetime.date | None = None
    due_date: datetime.date | None = None
    status: str | None = None
    file_url: str | None = None
    invoice: EmbeddedInvoice | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
