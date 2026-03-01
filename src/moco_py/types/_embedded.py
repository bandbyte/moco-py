"""Shared embedded (reference) models used across multiple resource types."""

from __future__ import annotations

from pydantic import BaseModel


class EmbeddedUserRef(BaseModel):
    """A lightweight user reference (id, firstname, lastname)."""

    id: int
    firstname: str
    lastname: str


class EmbeddedCompanyRef(BaseModel):
    """A lightweight company reference (id, name)."""

    id: int
    name: str


class EmbeddedDealRef(BaseModel):
    """A lightweight deal reference (id, name)."""

    id: int
    name: str


class EmbeddedInvoiceRef(BaseModel):
    """A lightweight invoice reference (id, identifier, title)."""

    id: int
    identifier: str | None = None
    title: str | None = None


class EmbeddedRevenueCategoryRef(BaseModel):
    """A lightweight revenue category reference."""

    id: int
    name: str
    revenue_account: int
    cost_category: str
