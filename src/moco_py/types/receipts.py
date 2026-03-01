"""Pydantic models for the Receipts resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import (
    EmbeddedCompanyRef as EmbeddedCompany,
)
from ._embedded import (
    EmbeddedUserRef as EmbeddedUser,
)


class EmbeddedVat(BaseModel):
    """VAT info embedded in a receipt item."""

    id: int
    tax: float
    reverse_charge: bool
    intra_eu: bool


class EmbeddedPurchaseCategory(BaseModel):
    """Purchase category embedded in a receipt item."""

    id: int
    name: str


class ReceiptItem(BaseModel):
    """An item (position) in a receipt."""

    gross_total: float
    vat: EmbeddedVat | None = None
    purchase_category: EmbeddedPurchaseCategory | None = None


class EmbeddedProject(BaseModel):
    """A project embedded in a receipt response."""

    id: int
    name: str
    billable: bool
    company: EmbeddedCompany | None = None


class EmbeddedRefundRequest(BaseModel):
    """A refund request embedded in a receipt response."""

    id: int
    status: str


class Receipt(BaseModel):
    """A receipt (expense) in MOCO."""

    id: int
    title: str
    date: datetime.date
    billable: bool | None = None
    pending: bool | None = None
    gross_total: float
    currency: str
    items: list[ReceiptItem] | None = None
    project: EmbeddedProject | None = None
    refund_request: EmbeddedRefundRequest | None = None
    info: str | None = None
    user: EmbeddedUser | None = None
    attachment_url: str | None = None
