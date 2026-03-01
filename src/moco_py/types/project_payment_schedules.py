"""Pydantic models for the Project Payment Schedules resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel


class EmbeddedProject(BaseModel):
    """A project embedded in a payment schedule response."""

    id: int
    identifier: str
    name: str


class ProjectPaymentSchedule(BaseModel):
    """A project payment schedule in MOCO."""

    id: int
    date: datetime.date
    title: str | None = None
    description: str | None = None
    net_total: float
    project: EmbeddedProject | None = None
    checked: bool
    billed: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
