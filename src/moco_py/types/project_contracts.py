"""Pydantic models for the Project Contracts resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ProjectContract(BaseModel):
    """A project contract (staff assignment) in MOCO."""

    id: int
    user_id: int
    firstname: str
    lastname: str
    billable: bool
    active: bool
    budget: float | None = None
    hourly_rate: float
    created_at: datetime
    updated_at: datetime
