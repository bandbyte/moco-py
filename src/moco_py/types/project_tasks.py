"""Pydantic models for the Project Tasks resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedRevenueCategoryRef as EmbeddedRevenueCategory


class ProjectTask(BaseModel):
    """A project task (service) in MOCO."""

    id: int
    name: str
    billable: bool
    active: bool
    budget: float | None = None
    hourly_rate: float
    revenue_category: EmbeddedRevenueCategory | None = None
    description: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
