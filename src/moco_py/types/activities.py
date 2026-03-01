"""Pydantic models for the Activities resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel, field_validator

from ._embedded import EmbeddedUserRef as EmbeddedUser
from ._enums import RemoteService


class EmbeddedProject(BaseModel):
    """A project embedded in an activity response."""

    id: int
    name: str
    billable: bool


class EmbeddedTask(BaseModel):
    """A task embedded in an activity response."""

    id: int
    name: str
    billable: bool


class EmbeddedCustomer(BaseModel):
    """A customer embedded in an activity response."""

    id: int
    name: str


class Activity(BaseModel):
    """An activity (time entry) in MOCO."""

    id: int
    date: datetime.date
    hours: float
    seconds: int
    worked_seconds: int
    description: str
    billed: bool
    invoice_id: int | None
    billable: bool
    tag: str
    remote_service: RemoteService | None = None
    remote_id: str | None = None
    remote_url: str | None = None
    project: EmbeddedProject
    task: EmbeddedTask
    customer: EmbeddedCustomer
    user: EmbeddedUser
    hourly_rate: float
    timer_started_at: str | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @field_validator("remote_service", mode="before")
    @classmethod
    def _empty_remote_service_to_none(cls, v: object) -> object:
        return None if v == "" else v
