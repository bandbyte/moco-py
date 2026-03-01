"""Pydantic models for the User Permission Roles resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class RolePermission(BaseModel):
    """Permission details for a user role."""

    report: str
    companies: str
    contacts: str
    people: str
    purchases: str
    settings: str
    sales: str
    projects: str
    calendar: str
    time_tracking: str
    invoicing: str


class UserRole(BaseModel):
    """A user permission role in MOCO."""

    id: int
    name: str
    is_default: bool
    is_admin: bool
    permission: RolePermission
    created_at: datetime
    updated_at: datetime
