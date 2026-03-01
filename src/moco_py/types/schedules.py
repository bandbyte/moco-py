"""Pydantic models for the Schedules (Absences) resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from moco_py.types._enums import ScheduleSymbol


class ScheduleAssignment(BaseModel):
    """An assignment (absence) embedded in a schedule response."""

    id: int
    name: str
    code: str
    customer_name: str | None = None
    color: str | None = None
    type: str


class ScheduleUser(BaseModel):
    """A user embedded in a schedule response."""

    id: int
    firstname: str
    lastname: str


class Schedule(BaseModel):
    """A schedule (absence) entry in MOCO."""

    id: int
    date: datetime.date
    comment: str | None = None
    am: bool
    pm: bool
    symbol: ScheduleSymbol | None = None
    assignment: ScheduleAssignment
    user: ScheduleUser
    created_at: datetime.datetime
    updated_at: datetime.datetime
