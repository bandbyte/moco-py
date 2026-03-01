"""Pydantic models for the Reports resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel


class ReportUnit(BaseModel):
    """A unit embedded in a report user."""

    id: int
    name: str


class ReportUser(BaseModel):
    """A user embedded in a report entry."""

    id: int
    firstname: str
    lastname: str | None = None
    name: str | None = None
    initials: str | None = None
    color: str | None = None
    unit: ReportUnit | None = None


class AbsenceEntry(BaseModel):
    """An entry in the absences report."""

    user: ReportUser
    total_vacation_days: float
    used_vacation_days: float
    planned_vacation_days: float
    sickdays: float


class CashflowCompany(BaseModel):
    """A company embedded in a cashflow entry."""

    id: int
    name: str


class CashflowEntry(BaseModel):
    """An entry in the cashflow report."""

    record_id: int
    company_id: int | None = None
    description: str | None = None
    user_id: int | None = None
    amount_in_account_currency: float
    kind: str
    company: CashflowCompany | None = None
    user: ReportUser | None = None
    date: datetime.date


class FinanceEntry(BaseModel):
    """An entry in the finance report."""

    record_id: int
    company_id: int | None = None
    description: str | None = None
    user_id: int | None = None
    net_amount_in_account_currency: float
    kind: str
    company: CashflowCompany | None = None
    user: ReportUser | None = None
    date: datetime.date


class PlannedVsTrackedProjectCompany(BaseModel):
    """A company embedded in a planned vs tracked project."""

    id: int
    name: str


class PlannedVsTrackedProject(BaseModel):
    """A project embedded in a planned vs tracked entry."""

    id: int
    identifier: str | None = None
    name: str
    company: PlannedVsTrackedProjectCompany | None = None


class PlannedVsTrackedEntry(BaseModel):
    """An entry in the planned vs tracked report."""

    user_id: int
    project_id: int
    tracked_hours: float
    planned_hours: float
    delta: float
    quota: float
    user: ReportUser | None = None
    project: PlannedVsTrackedProject | None = None


class UtilizationEntry(BaseModel):
    """An entry in the utilization report."""

    date: datetime.date
    user_id: int
    target_hours: float
    billable_hours: float
    unbillable_hours: float
    billable_seconds: float
    unbillable_seconds: float
