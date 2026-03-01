"""Pydantic models for the Companies resource."""

from __future__ import annotations

import datetime
from typing import Any

from pydantic import BaseModel

from ._embedded import EmbeddedUserRef as EmbeddedUser
from ._enums import CompanyType


class EmbeddedProject(BaseModel):
    """A project embedded in a company response."""

    id: int
    identifier: str
    name: str
    active: bool
    billable: bool


class CustomerVat(BaseModel):
    """Customer VAT settings."""

    tax: float
    reverse_charge: bool
    intra_eu: bool
    active: bool
    print_gross_total: bool
    notice_tax_exemption: str
    notice_tax_exemption_alt: str


class SupplierVat(BaseModel):
    """Supplier VAT settings."""

    tax: float
    reverse_charge: bool
    intra_eu: bool
    active: bool


class Company(BaseModel):
    """A company in MOCO."""

    id: int
    type: CompanyType
    name: str
    website: str | None = None
    email: str | None = None
    billing_email_cc: str | None = None
    phone: str | None = None
    fax: str | None = None
    address: str | None = None
    tags: list[str]
    user: EmbeddedUser | None = None
    info: str | None = None
    custom_properties: dict[str, Any] | None = None
    identifier: str | None = None
    intern: bool
    billing_tax: float | None = None
    customer_vat: CustomerVat | None = None
    supplier_vat: SupplierVat | None = None
    currency: str | None = None
    custom_rates: bool | None = None
    include_time_report: bool | None = None
    billing_notes: str | None = None
    default_discount: float | None = None
    default_cash_discount: float | None = None
    default_cash_discount_days: int | None = None
    country_code: str | None = None
    vat_identifier: str | None = None
    alternative_correspondence_language: bool | None = None
    default_invoice_due_days: int | None = None
    footer: str | None = None
    projects: list[EmbeddedProject] | None = None
    active: bool
    archived_on: datetime.date | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    debit_number: int | None = None
