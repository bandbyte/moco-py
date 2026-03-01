"""Pydantic models for the Projects resource."""

from __future__ import annotations

import datetime
from typing import Any

from pydantic import BaseModel

from ._embedded import (
    EmbeddedCompanyRef as EmbeddedCustomer,
)
from ._enums import BillingVariant
from ._embedded import (
    EmbeddedDealRef as EmbeddedDeal,
)
from ._embedded import (
    EmbeddedUserRef as EmbeddedContact,
)
from ._embedded import (
    EmbeddedUserRef as EmbeddedLeader,
)


class EmbeddedProjectTask(BaseModel):
    """A task embedded in a project response."""

    id: int
    name: str
    billable: bool
    active: bool
    budget: float | None = None
    hourly_rate: float
    description: str | None = None


class EmbeddedProjectContract(BaseModel):
    """A contract embedded in a project response."""

    id: int
    user_id: int
    firstname: str
    lastname: str
    billable: bool
    active: bool
    budget: float | None = None
    hourly_rate: float


class EmbeddedProjectGroup(BaseModel):
    """A project group embedded in a project response."""

    id: int
    name: str


class Project(BaseModel):
    """A project in MOCO."""

    id: int
    identifier: str
    name: str
    active: bool
    billable: bool
    fixed_price: bool
    retainer: bool
    start_date: datetime.date | None = None
    finish_date: datetime.date | None = None
    color: str | None = None
    currency: str
    billing_variant: BillingVariant | None = None
    billing_address: str | None = None
    billing_email_to: str | None = None
    billing_email_cc: str | None = None
    billing_notes: str | None = None
    setting_include_time_report: bool | None = None
    budget: float | None = None
    budget_monthly: float | None = None
    budget_expenses: float | None = None
    hourly_rate: float | None = None
    info: str | None = None
    tags: list[str] | None = None
    customer_report_url: str | None = None
    custom_properties: dict[str, Any] | None = None
    leader: EmbeddedLeader | None = None
    co_leader: EmbeddedLeader | None = None
    customer: EmbeddedCustomer | None = None
    deal: EmbeddedDeal | None = None
    tasks: list[EmbeddedProjectTask] | None = None
    contracts: list[EmbeddedProjectContract] | None = None
    project_group: EmbeddedProjectGroup | None = None
    billing_contact: EmbeddedContact | None = None
    contact: EmbeddedContact | None = None
    secondary_contact: EmbeddedContact | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class AssignedProjectTask(BaseModel):
    """A task in an assigned project response."""

    id: int
    name: str
    active: bool
    billable: bool


class AssignedProjectContract(BaseModel):
    """A contract in an assigned project response."""

    user_id: int
    active: bool


class AssignedProject(BaseModel):
    """An assigned project in MOCO (limited info)."""

    id: int
    identifier: str
    name: str
    active: bool
    billable: bool
    customer: EmbeddedCustomer
    tasks: list[AssignedProjectTask]
    contract: AssignedProjectContract


class CostByTask(BaseModel):
    """Cost breakdown by task in a project report."""

    id: int
    name: str
    hours_total: float
    total_costs: float


class ProjectReport(BaseModel):
    """A project report in MOCO."""

    budget_total: float | None = None
    budget_progress_in_percentage: float | None = None
    budget_remaining: float | None = None
    invoiced_total: float | None = None
    currency: str
    hours_total: float
    hours_billable: float
    hours_remaining: float
    costs_expenses: float | None = None
    costs_activities: float | None = None
    costs_by_task: list[CostByTask] | None = None


class ProjectShareResponse(BaseModel):
    """Response from share/disable_share endpoints."""

    id: int
    active: bool
    url: str | None = None
