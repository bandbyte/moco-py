"""Pydantic models for the Contacts (People) resource."""

from __future__ import annotations

import datetime

from pydantic import BaseModel

from ._embedded import EmbeddedCompanyRef
from ._enums import Gender


class EmbeddedCompany(EmbeddedCompanyRef):
    """A company embedded in a contact response (includes type)."""

    type: str


class Contact(BaseModel):
    """A contact (person) in MOCO."""

    id: int
    gender: Gender | None = None
    firstname: str | None = None
    lastname: str
    title: str | None = None
    job_position: str | None = None
    mobile_phone: str | None = None
    work_fax: str | None = None
    work_phone: str | None = None
    work_email: str | None = None
    work_address: str | None = None
    home_email: str | None = None
    home_address: str | None = None
    birthday: datetime.date | None = None
    info: str | None = None
    avatar_url: str | None = None
    tags: list[str] | None = None
    company: EmbeddedCompany | None = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
