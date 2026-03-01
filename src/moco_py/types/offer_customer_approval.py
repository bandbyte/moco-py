"""Pydantic models for the Offer Customer Approval resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel


class OfferCustomerApproval(BaseModel):
    """An offer customer approval in MOCO."""

    id: int
    approval_url: str | None = None
    offer_document_url: str | None = None
    active: bool | None = None
    customer_full_name: str | None = None
    customer_email: str | None = None
    signature_url: str | None = None
    signed_at: datetime.datetime | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
