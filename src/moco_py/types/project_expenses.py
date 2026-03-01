"""Pydantic models for the Project Expenses resource."""

from __future__ import annotations

import datetime
from typing import Any

from pydantic import BaseModel

from ._embedded import (
    EmbeddedCompanyRef as EmbeddedCompany,
)
from ._embedded import (
    EmbeddedRevenueCategoryRef as EmbeddedRevenueCategory,
)


class EmbeddedProject(BaseModel):
    """A project embedded in an expense response."""

    id: int
    name: str


class EmbeddedExpenseGroup(BaseModel):
    """A group embedded in an expense response."""

    id: int
    title: str
    budget: float | None = None


class EmbeddedPurchaseDocument(BaseModel):
    """A document embedded in a purchase item."""

    id: int
    file_url: str | None = None


class EmbeddedPurchaseItem(BaseModel):
    """A purchase item embedded in an expense response."""

    id: int
    title: str
    net_total: float
    currency: str
    purchase_id: int
    document: EmbeddedPurchaseDocument | None = None


class ProjectExpense(BaseModel):
    """A project expense (additional service) in MOCO."""

    id: int
    date: datetime.date
    title: str
    description: str | None = None
    quantity: float
    unit: str
    unit_price: float
    unit_cost: float
    price: float
    cost: float
    currency: str
    budget_relevant: bool
    billable: bool
    billed: bool
    purchase_assignment_locked: bool | None = None
    cost_total_planned: float | None = None
    planned_purchase_date: datetime.date | None = None
    invoice_id: int | None = None
    recurring_expense_id: int | None = None
    service_period: str | None = None
    service_period_from: datetime.date | None = None
    service_period_to: datetime.date | None = None
    file_url: str | None = None
    revenue_category: EmbeddedRevenueCategory | None = None
    custom_properties: dict[str, Any] | None = None
    company: EmbeddedCompany | None = None
    project: EmbeddedProject | None = None
    group: EmbeddedExpenseGroup | None = None
    purchase_items: list[EmbeddedPurchaseItem] | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
