"""Pydantic models for the Invoice Bookkeeping Exports resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel, Field

from ._embedded import EmbeddedUserRef as EmbeddedUser


class InvoiceBookkeepingExport(BaseModel):
    """An invoice bookkeeping export in MOCO."""

    id: int
    from_date: datetime.date | None = Field(None, alias="from")
    to_date: datetime.date | None = Field(None, alias="to")
    invoice_ids: list[int] | None = None
    comment: str | None = None
    user: EmbeddedUser | None = None
    status: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = {"populate_by_name": True}
