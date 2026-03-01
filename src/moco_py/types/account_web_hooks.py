"""Pydantic models for the Account Web Hooks resource."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from moco_py.types._enums import WebhookEvent, WebhookTarget


class WebHook(BaseModel):
    """A web hook in MOCO."""

    id: int
    target: WebhookTarget
    event: WebhookEvent
    hook: str
    disabled: bool
    disabled_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
