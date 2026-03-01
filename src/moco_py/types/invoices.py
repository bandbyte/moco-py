"""Pydantic models for the Invoices resource."""

from __future__ import annotations

import datetime
from typing import Any

from pydantic import BaseModel

from ._embedded import EmbeddedUserRef as EmbeddedUser
from ._enums import InvoiceStatus, ItemType, ServiceType


class RevenueCategory(BaseModel):
    """Revenue category for an invoice item."""

    id: int
    name: str
    revenue_account: int | None = None
    cost_category: str | None = None


class InvoiceItem(BaseModel):
    """A line item / position on an invoice."""

    id: int
    type: ItemType
    title: str | None = None
    revenue_category: RevenueCategory | None = None
    description: str | None = None
    quantity: float | None = None
    unit: str | None = None
    unit_price: float | None = None
    net_total: float | None = None
    optional: bool | None = None
    additional: bool | None = None
    service_type: ServiceType | None = None
    expense_ids: list[int] | None = None


class InvoicePaymentEntry(BaseModel):
    """An embedded payment on an invoice."""

    id: int
    date: datetime.date
    paid_total: float
    currency: str
    created_on: datetime.date | None = None
    updated_on: datetime.date | None = None


class InvoiceReminderEntry(BaseModel):
    """An embedded reminder on an invoice."""

    id: int
    date: datetime.date
    due_date: datetime.date
    fee: float | None = None
    text: str | None = None
    created_on: datetime.date | None = None
    updated_on: datetime.date | None = None


class InvoiceVat(BaseModel):
    """VAT details for an invoice."""

    tax: float | None = None
    reverse_charge: bool | None = None
    intra_eu: bool | None = None
    active: bool | None = None
    print_gross_total: bool | None = None
    notice_tax_exemption: str | None = None
    notice_tax_exemption_alt: str | None = None
    code: str | None = None


class Invoice(BaseModel):
    """An invoice in MOCO."""

    id: int
    customer_id: int | None = None
    project_id: int | None = None
    offer_id: int | None = None
    identifier: str | None = None
    date: datetime.date | None = None
    due_date: datetime.date | None = None
    service_period: str | None = None
    service_period_from: datetime.date | None = None
    service_period_to: datetime.date | None = None
    status: InvoiceStatus | None = None
    reversed: bool | None = None
    reversal_invoice_id: int | None = None
    reversal: bool | None = None
    reversed_invoice_id: int | None = None
    title: str | None = None
    recipient_address: str | None = None
    currency: str | None = None
    net_total: float | None = None
    tax: float | None = None
    vat: InvoiceVat | None = None
    gross_total: float | None = None
    discount: float | None = None
    creditor_reference: str | None = None
    cash_discount: float | None = None
    cash_discount_days: int | None = None
    debit_number: str | None = None
    credit_number: str | None = None
    locked: bool | None = None
    activity_hours_modified: bool | None = None
    salutation: str | None = None
    footer: str | None = None
    custom_properties: dict[str, str] | None = None
    tags: list[str] | None = None
    file_url: str | None = None
    user: EmbeddedUser | None = None
    items: list[InvoiceItem] | None = None
    payments: list[InvoicePaymentEntry] | None = None
    reminders: list[InvoiceReminderEntry] | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class InvoiceTimesheetActivity(BaseModel):
    """An activity from an invoice timesheet."""

    id: int
    date: datetime.date
    hours: float
    description: str | None = None
    billed: bool | None = None
    billable: bool | None = None
    tag: str | None = None
    remote_service: str | None = None
    remote_id: str | None = None
    remote_url: str | None = None
    project: dict[str, Any] | None = None
    task: dict[str, Any] | None = None
    customer: dict[str, Any] | None = None
    user: EmbeddedUser | None = None
    timer_started_at: str | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
    hourly_rate: float | None = None


class InvoiceExpense(BaseModel):
    """An expense from an invoice."""

    id: int
    date: datetime.date | None = None
    title: str | None = None
    description: str | None = None
    quantity: float | None = None
    unit: str | None = None
    unit_price: float | None = None
    unit_cost: float | None = None
    price: float | None = None
    cost: float | None = None
    currency: str | None = None
    budget_relevant: bool | None = None
    billable: bool | None = None
    billed: bool | None = None
    recurring_expense_id: int | None = None
    service_period: str | None = None
    service_period_from: datetime.date | None = None
    service_period_to: datetime.date | None = None
    file_url: str | None = None
    custom_properties: dict[str, str] | None = None
    company: dict[str, Any] | None = None
    project: dict[str, Any] | None = None
    purchase_id: int | None = None
    purchase_item_id: int | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
