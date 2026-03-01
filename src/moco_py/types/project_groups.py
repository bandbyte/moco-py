"""Pydantic models for the Project Groups resource."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel


class ProjectGroupUser(BaseModel):
    """A user embedded in a project group response."""

    id: int
    firstname: str
    lastname: str


class ProjectGroupCompany(BaseModel):
    """A company embedded in a project group response."""

    id: int
    name: str


class ProjectGroupProject(BaseModel):
    """A project embedded in a project group response."""

    id: int
    identifier: str
    name: str
    active: bool
    budget: float


class ProjectGroup(BaseModel):
    """A project group in MOCO."""

    id: int
    name: str
    user: ProjectGroupUser | None = None
    company: ProjectGroupCompany | None = None
    budget: float | None = None
    currency: str | None = None
    info: str | None = None
    custom_properties: dict[str, Any] | None = None
    customer_report_url: str | None = None
    projects: list[ProjectGroupProject] | None = None
    created_at: datetime
    updated_at: datetime
