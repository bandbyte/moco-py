"""Pydantic models for the Purchase Budgets resource."""

from __future__ import annotations

from pydantic import BaseModel


class PurchaseBudget(BaseModel):
    """A purchase budget in MOCO."""

    id: str
    year: int | None = None
    title: str | None = None
    active: bool | None = None
    target: float | None = None
    exhaused: float | None = None
    planned: float | None = None
    remaining: float | None = None
