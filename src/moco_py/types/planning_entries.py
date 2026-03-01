"""Pydantic models for the Planning Entries resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from moco_py.types._enums import PlanningSymbol

from ._embedded import EmbeddedUserRef as EmbeddedUser


class EmbeddedProject(BaseModel):
    """A project embedded in a planning entry response."""

    id: int
    identifier: str
    name: str
    customer_name: str
    color: str


class EmbeddedTask(BaseModel):
    """A task embedded in a planning entry response."""

    id: int
    name: str


class EmbeddedDeal(BaseModel):
    """A deal embedded in a planning entry response."""

    id: int
    name: str
    customer_name: str
    color: str


class PlanningEntry(BaseModel):
    """A planning entry in MOCO."""

    id: int
    title: str | None = None
    starts_on: datetime.date
    ends_on: datetime.date
    hours_per_day: float
    comment: str | None = None
    symbol: PlanningSymbol | None = None
    color: str | None = None
    read_only: bool | None = None
    user: EmbeddedUser | None = None
    project: EmbeddedProject | None = None
    task: EmbeddedTask | None = None
    deal: EmbeddedDeal | None = None
    series_id: int | None = None
    tentative: bool | None = None
    series_repeat: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
