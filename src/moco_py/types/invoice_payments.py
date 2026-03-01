"""Pydantic models for the Invoice Payments resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedInvoiceRef as EmbeddedInvoice


class InvoicePayment(BaseModel):
    """An invoice payment in MOCO."""

    id: int
    date: datetime.date
    invoice: EmbeddedInvoice | None = None
    paid_total: float | str
    paid_total_in_account_currency: float | str | None = None
    currency: str | None = None
    description: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
