"""Pydantic models for the Users resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel


class EmbeddedUnit(BaseModel):
    """A unit embedded in a user response."""

    id: int
    name: str


class EmbeddedRole(BaseModel):
    """A role embedded in a user response."""

    id: int
    name: str


class User(BaseModel):
    """A user (staff member) in MOCO."""

    id: int
    firstname: str
    lastname: str
    active: bool
    extern: bool
    email: str
    mobile_phone: str | None = None
    work_phone: str | None = None
    home_address: str | None = None
    info: str | None = None
    birthday: datetime.date | None = None
    iban: str | None = None
    avatar_url: str | None = None
    tags: list[str] = []
    custom_properties: dict[str, str] | None = None
    unit: EmbeddedUnit | None = None
    role: EmbeddedRole | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class PerformanceReportAnnually(BaseModel):
    """Annual performance report data."""

    year: int
    employment_hours: float
    target_hours: float
    hours_tracked_total: float
    variation: float
    variation_until_today: float
    hours_billable_total: float


class PerformanceReportMonthly(BaseModel):
    """Monthly performance report data."""

    year: int
    month: int
    target_hours: float
    hours_tracked_total: float
    variation: float
    hours_billable_total: float


class PerformanceReport(BaseModel):
    """Performance report for a user."""

    annually: PerformanceReportAnnually
    monthly: list[PerformanceReportMonthly]
