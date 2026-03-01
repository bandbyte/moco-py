"""Pydantic models for the Project Recurring Expenses resource."""

from __future__ import annotations

import datetime
from typing import Any

from pydantic import BaseModel

from ._embedded import EmbeddedRevenueCategoryRef as EmbeddedRevenueCategory


class EmbeddedProject(BaseModel):
    """A project embedded in a recurring expense response."""

    id: int
    name: str


class ProjectRecurringExpense(BaseModel):
    """A project recurring expense in MOCO."""

    id: int
    start_date: datetime.date
    finish_date: datetime.date | None = None
    recur_next_date: datetime.date | None = None
    period: str
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
    service_period_direction: str | None = None
    custom_properties: dict[str, Any] | None = None
    project: EmbeddedProject | None = None
    revenue_category: EmbeddedRevenueCategory | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
