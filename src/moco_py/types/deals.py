"""Pydantic models for the Deals (Leads) resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedCompanyRef
from ._embedded import EmbeddedUserRef as EmbeddedUser
from ._enums import DealStatus


class EmbeddedCompany(EmbeddedCompanyRef):
    """A company embedded in a deal response (includes type)."""

    type: str


class EmbeddedPerson(BaseModel):
    """A person embedded in a deal response."""

    id: int
    name: str


class EmbeddedCategory(BaseModel):
    """A category embedded in a deal response."""

    id: int
    name: str
    probability: int


class Deal(BaseModel):
    """A deal (lead) in MOCO."""

    id: int
    name: str
    status: DealStatus
    reminder_date: datetime.date | None = None
    closed_on: datetime.date | None = None
    money: float
    currency: str
    info: str | None = None
    custom_properties: dict[str, str] | None = None
    user: EmbeddedUser | None = None
    company: EmbeddedCompany | None = None
    person: EmbeddedPerson | None = None
    category: EmbeddedCategory | None = None
    service_period_from: datetime.date | None = None
    service_period_to: datetime.date | None = None
    inbox_email_address: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
