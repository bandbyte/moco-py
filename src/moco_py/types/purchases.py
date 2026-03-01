"""Pydantic models for the Purchases resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from moco_py.types._enums import ApprovalStatus, PaymentMethod, PurchaseStatus


class PurchaseCompany(BaseModel):
    """A company (supplier) embedded in a purchase."""

    id: int
    name: str
    iban: str | None = None


class PurchaseUser(BaseModel):
    """A user embedded in a purchase."""

    id: int
    firstname: str
    name: str


class PurchasePaymentEntry(BaseModel):
    """A payment entry embedded in a purchase."""

    id: int
    date: datetime.date
    total: float


class PurchaseVat(BaseModel):
    """VAT details for a purchase item."""

    tax: float
    reverse_charge: bool
    intra_eu: bool
    active: bool
    code: str | None = None


class PurchaseItemCategory(BaseModel):
    """Category embedded in a purchase item."""

    id: int
    name: str
    credit_account: str | None = None


class PurchaseItemExpenseProject(BaseModel):
    """Project embedded in a purchase item expense."""

    id: int
    company_id: int | None = None


class PurchaseItemExpense(BaseModel):
    """Expense embedded in a purchase item."""

    id: int
    project: PurchaseItemExpenseProject | None = None


class PurchaseItemReceipt(BaseModel):
    """Receipt embedded in a purchase item."""

    id: int
    title: str | None = None
    date: datetime.date | None = None
    attachment_url: str | None = None


class PurchaseItem(BaseModel):
    """A line item in a purchase."""

    id: int
    title: str
    net_total: float
    tax_total: float | None = None
    tax: float
    vat: PurchaseVat | None = None
    tax_included: bool | None = None
    gross_total: float
    category: PurchaseItemCategory | None = None
    supplier_credit_number: int | None = None
    expense: PurchaseItemExpense | None = None
    receipt: PurchaseItemReceipt | None = None


class RefundRequest(BaseModel):
    """Refund request embedded in a purchase."""

    id: int
    comment: str | None = None
    user_id: int | None = None


class CreditCardTransaction(BaseModel):
    """Credit card transaction embedded in a purchase."""

    source: str | None = None
    transaction_identifier: str | None = None


class Purchase(BaseModel):
    """A purchase in MOCO."""

    id: int
    identifier: str | None = None
    receipt_identifier: str | None = None
    title: str | None = None
    info: str | None = None
    iban: str | None = None
    reference: str | None = None
    date: datetime.date | None = None
    due_date: datetime.date | None = None
    service_period_from: datetime.date | None = None
    service_period_to: datetime.date | None = None
    status: PurchaseStatus | None = None
    payment_method: PaymentMethod | None = None
    net_total: float | None = None
    gross_total: float | None = None
    currency: str | None = None
    file_url: str | None = None
    custom_properties: dict[str, str] | None = None
    tags: list[str] | None = None
    approval_status: ApprovalStatus | None = None
    company: PurchaseCompany | None = None
    payments: list[PurchasePaymentEntry] | None = None
    user: PurchaseUser | None = None
    refund_request: RefundRequest | None = None
    credit_card_transaction: CreditCardTransaction | None = None
    items: list[PurchaseItem] | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
