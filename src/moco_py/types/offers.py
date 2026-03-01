"""Pydantic models for the Offers resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import (
    EmbeddedCompanyRef as EmbeddedCompany,
)
from ._enums import ItemType, OfferStatus, ServiceType
from ._embedded import (
    EmbeddedDealRef as EmbeddedDeal,
)
from ._embedded import (
    EmbeddedUserRef as EmbeddedUser,
)


class EmbeddedProject(BaseModel):
    """A project embedded in an offer response."""

    id: int
    identifier: str | None = None
    name: str


class OfferConfirmation(BaseModel):
    """Offer confirmation details."""

    id: int
    date: datetime.date | None = None
    title: str | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None


class CustomerApproval(BaseModel):
    """Customer approval details on an offer."""

    id: int
    active: bool | None = None
    url: str | None = None


class RevenueCategory(BaseModel):
    """Revenue category for an offer item."""

    id: int
    name: str
    revenue_account: int | None = None
    cost_category: str | None = None


class OfferVat(BaseModel):
    """VAT details for an offer."""

    tax: float | None = None
    reverse_charge: bool | None = None
    intra_eu: bool | None = None
    active: bool | None = None
    print_gross_total: bool | None = None
    notice_tax_exemption: str | None = None
    notice_tax_exemption_alt: str | None = None
    code: str | None = None


class OfferItem(BaseModel):
    """A line item / position on an offer."""

    id: int
    type: ItemType
    title: str | None = None
    description: str | None = None
    quantity: float | None = None
    unit: str | None = None
    unit_price: float | None = None
    unit_cost: float | None = None
    net_total: float | None = None
    optional: bool | None = None
    service_type: ServiceType | None = None
    revenue_category: RevenueCategory | None = None


class Offer(BaseModel):
    """An offer in MOCO."""

    id: int
    identifier: str | None = None
    invoice_id: int | None = None
    date: datetime.date | None = None
    due_date: datetime.date | None = None
    title: str | None = None
    recipient_address: str | None = None
    currency: str | None = None
    net_total: float | None = None
    tax: float | None = None
    vat: OfferVat | None = None
    gross_total: float | None = None
    discount: float | None = None
    status: OfferStatus | None = None
    salutation: str | None = None
    footer: str | None = None
    tags: list[str] | None = None
    custom_properties: dict[str, str] | None = None
    company: EmbeddedCompany | None = None
    project: EmbeddedProject | None = None
    deal: EmbeddedDeal | None = None
    user: EmbeddedUser | None = None
    offer_confirmation: OfferConfirmation | None = None
    customer_approval: CustomerApproval | None = None
    items: list[OfferItem] | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
