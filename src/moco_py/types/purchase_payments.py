"""Pydantic models for the Purchase Payments resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel


class PurchasePaymentPurchase(BaseModel):
    """A purchase embedded in a purchase payment."""

    id: int
    identifier: str | None = None
    title: str | None = None


class PurchasePayment(BaseModel):
    """A purchase payment in MOCO."""

    id: int
    date: datetime.date
    purchase: PurchasePaymentPurchase | None = None
    total: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
