"""Invoice Reminders resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.invoice_reminders import InvoiceReminder


def _filter_params(
    *,
    invoice_id: int | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
) -> dict[str, Any] | None:
    params: dict[str, Any] = {}
    if invoice_id is not None:
        params["invoice_id"] = invoice_id
    if date_from is not None:
        params["date_from"] = date_from
    if date_to is not None:
        params["date_to"] = date_to
    return params or None


class InvoiceReminders(SyncResource):
    """Synchronous invoice reminders resource."""

    def list(
        self,
        *,
        invoice_id: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> SyncPage[InvoiceReminder]:
        """Retrieve all invoice reminders."""
        params = _filter_params(
            invoice_id=invoice_id, date_from=date_from, date_to=date_to
        )
        return self._get_list(
            "/invoice_reminders", params=params, cast_to=InvoiceReminder
        )

    def get(self, reminder_id: int) -> MocoResponse[InvoiceReminder]:
        """Retrieve a single invoice reminder."""
        return self._get(f"/invoice_reminders/{reminder_id}", cast_to=InvoiceReminder)

    def create(
        self,
        *,
        invoice_id: int,
        title: str | None = None,
        text: str | None = None,
        fee: float | None = None,
        date: str | None = None,
        due_date: str | None = None,
    ) -> MocoResponse[InvoiceReminder]:
        """Create an invoice reminder."""
        data: dict[str, Any] = {"invoice_id": invoice_id}
        if title is not None:
            data["title"] = title
        if text is not None:
            data["text"] = text
        if fee is not None:
            data["fee"] = fee
        if date is not None:
            data["date"] = date
        if due_date is not None:
            data["due_date"] = due_date
        return self._post("/invoice_reminders", json_data=data, cast_to=InvoiceReminder)

    def delete(self, reminder_id: int) -> MocoResponse[None]:
        """Delete an invoice reminder."""
        return self._delete(f"/invoice_reminders/{reminder_id}")

    def send_email(
        self,
        reminder_id: int,
        *,
        subject: str,
        text: str,
        emails_to: str | None = None,
        emails_cc: str | None = None,
        emails_bcc: str | None = None,
    ) -> MocoResponse[None]:
        """Send the reminder by email."""
        data: dict[str, Any] = {"subject": subject, "text": text}
        if emails_to is not None:
            data["emails_to"] = emails_to
        if emails_cc is not None:
            data["emails_cc"] = emails_cc
        if emails_bcc is not None:
            data["emails_bcc"] = emails_bcc
        return self._post(
            f"/invoice_reminders/{reminder_id}/send_email",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )


class AsyncInvoiceReminders(AsyncResource):
    """Asynchronous invoice reminders resource."""

    async def list(
        self,
        *,
        invoice_id: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> AsyncPage[InvoiceReminder]:
        """Retrieve all invoice reminders."""
        params = _filter_params(
            invoice_id=invoice_id, date_from=date_from, date_to=date_to
        )
        return await self._get_list(
            "/invoice_reminders", params=params, cast_to=InvoiceReminder
        )

    async def get(self, reminder_id: int) -> MocoResponse[InvoiceReminder]:
        """Retrieve a single invoice reminder."""
        return await self._get(
            f"/invoice_reminders/{reminder_id}", cast_to=InvoiceReminder
        )

    async def create(
        self,
        *,
        invoice_id: int,
        title: str | None = None,
        text: str | None = None,
        fee: float | None = None,
        date: str | None = None,
        due_date: str | None = None,
    ) -> MocoResponse[InvoiceReminder]:
        """Create an invoice reminder."""
        data: dict[str, Any] = {"invoice_id": invoice_id}
        if title is not None:
            data["title"] = title
        if text is not None:
            data["text"] = text
        if fee is not None:
            data["fee"] = fee
        if date is not None:
            data["date"] = date
        if due_date is not None:
            data["due_date"] = due_date
        return await self._post(
            "/invoice_reminders", json_data=data, cast_to=InvoiceReminder
        )

    async def delete(self, reminder_id: int) -> MocoResponse[None]:
        """Delete an invoice reminder."""
        return await self._delete(f"/invoice_reminders/{reminder_id}")

    async def send_email(
        self,
        reminder_id: int,
        *,
        subject: str,
        text: str,
        emails_to: str | None = None,
        emails_cc: str | None = None,
        emails_bcc: str | None = None,
    ) -> MocoResponse[None]:
        """Send the reminder by email."""
        data: dict[str, Any] = {"subject": subject, "text": text}
        if emails_to is not None:
            data["emails_to"] = emails_to
        if emails_cc is not None:
            data["emails_cc"] = emails_cc
        if emails_bcc is not None:
            data["emails_bcc"] = emails_bcc
        return await self._post(
            f"/invoice_reminders/{reminder_id}/send_email",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )
