"""Invoices resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import InvoiceChangeAddress, InvoiceStatus
from ..types.invoices import Invoice, InvoiceExpense, InvoiceTimesheetActivity


def _filter_params(
    *,
    status: InvoiceStatus | None = None,
    include_disregarded: bool | None = None,
    not_booked: bool | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    service_period_from: str | None = None,
    service_period_to: str | None = None,
    tags: str | None = None,
    identifier: str | None = None,
    term: str | None = None,
    company_id: int | None = None,
    project_id: int | None = None,
) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    if include_disregarded is not None:
        params["include_disregarded"] = include_disregarded
    if not_booked is not None:
        params["not_booked"] = not_booked
    if date_from is not None:
        params["date_from"] = date_from
    if date_to is not None:
        params["date_to"] = date_to
    if service_period_from is not None:
        params["service_period_from"] = service_period_from
    if service_period_to is not None:
        params["service_period_to"] = service_period_to
    if tags is not None:
        params["tags"] = tags
    if identifier is not None:
        params["identifier"] = identifier
    if term is not None:
        params["term"] = term
    if company_id is not None:
        params["company_id"] = company_id
    if project_id is not None:
        params["project_id"] = project_id
    return params or None  # type: ignore[return-value]


class Invoices(SyncResource):
    """Synchronous invoices resource."""

    def list(
        self,
        *,
        status: InvoiceStatus | None = None,
        include_disregarded: bool | None = None,
        not_booked: bool | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        tags: str | None = None,
        identifier: str | None = None,
        term: str | None = None,
        company_id: int | None = None,
        project_id: int | None = None,
    ) -> SyncPage[Invoice]:
        """Retrieve all invoices."""
        params = _filter_params(
            status=status,
            include_disregarded=include_disregarded,
            not_booked=not_booked,
            date_from=date_from,
            date_to=date_to,
            service_period_from=service_period_from,
            service_period_to=service_period_to,
            tags=tags,
            identifier=identifier,
            term=term,
            company_id=company_id,
            project_id=project_id,
        )
        return self._get_list("/invoices", params=params, cast_to=Invoice)

    def locked(
        self,
        *,
        status: InvoiceStatus | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        identifier: str | None = None,
    ) -> SyncPage[Invoice]:
        """Retrieve all locked invoices."""
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        if date_from is not None:
            params["date_from"] = date_from
        if date_to is not None:
            params["date_to"] = date_to
        if identifier is not None:
            params["identifier"] = identifier
        return self._get_list(
            "/invoices/locked",
            params=params or None,
            cast_to=Invoice,
        )

    def get(self, invoice_id: int) -> MocoResponse[Invoice]:
        """Retrieve a single invoice."""
        return self._get(f"/invoices/{invoice_id}", cast_to=Invoice)

    def create(
        self,
        *,
        customer_id: int,
        recipient_address: str,
        date: str,
        due_date: str,
        title: str,
        tax: float,
        currency: str,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        status: InvoiceStatus | None = None,
        project_id: int | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        change_address: InvoiceChangeAddress | None = None,
        salutation: str | None = None,
        footer: str | None = None,
        discount: float | None = None,
        cash_discount: float | None = None,
        cash_discount_days: int | None = None,
        internal_contact_id: int | None = None,
        custom_properties: dict[str, str] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        print_detail_columns: bool | None = None,
    ) -> MocoResponse[Invoice]:
        """Create an invoice."""
        data: dict[str, Any] = {
            "customer_id": customer_id,
            "recipient_address": recipient_address,
            "date": date,
            "due_date": due_date,
            "title": title,
            "tax": tax,
            "currency": currency,
            "items": items,
        }
        if status is not None:
            data["status"] = status
        if project_id is not None:
            data["project_id"] = project_id
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if change_address is not None:
            data["change_address"] = change_address
        if salutation is not None:
            data["salutation"] = salutation
        if footer is not None:
            data["footer"] = footer
        if discount is not None:
            data["discount"] = discount
        if cash_discount is not None:
            data["cash_discount"] = cash_discount
        if cash_discount_days is not None:
            data["cash_discount_days"] = cash_discount_days
        if internal_contact_id is not None:
            data["internal_contact_id"] = internal_contact_id
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if tags is not None:
            data["tags"] = tags
        if print_detail_columns is not None:
            data["print_detail_columns"] = print_detail_columns
        return self._post("/invoices", json_data=data, cast_to=Invoice)

    def timesheet(self, invoice_id: int) -> SyncPage[InvoiceTimesheetActivity]:
        """Retrieve the timesheet for an invoice."""
        return self._get_list(
            f"/invoices/{invoice_id}/timesheet",
            cast_to=InvoiceTimesheetActivity,
        )

    def expenses(self, invoice_id: int) -> SyncPage[InvoiceExpense]:
        """Retrieve expenses for an invoice."""
        return self._get_list(
            f"/invoices/{invoice_id}/expenses",
            cast_to=InvoiceExpense,
        )

    def update_status(self, invoice_id: int, *, status: InvoiceStatus) -> MocoResponse[None]:
        """Update an invoice status."""
        return self._put(
            f"/invoices/{invoice_id}/update_status",
            json_data={"status": status},
            cast_to=None,  # type: ignore[arg-type]
        )

    def send_email(
        self,
        invoice_id: int,
        *,
        subject: str,
        text: str,
        emails_to: str | None = None,
        emails_cc: str | None = None,
        emails_bcc: str | None = None,
        letter_paper_id: int | None = None,
    ) -> MocoResponse[None]:
        """Send the invoice by email."""
        data: dict[str, Any] = {"subject": subject, "text": text}
        if emails_to is not None:
            data["emails_to"] = emails_to
        if emails_cc is not None:
            data["emails_cc"] = emails_cc
        if emails_bcc is not None:
            data["emails_bcc"] = emails_bcc
        if letter_paper_id is not None:
            data["letter_paper_id"] = letter_paper_id
        return self._post(
            f"/invoices/{invoice_id}/send_email",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )

    def delete(
        self, invoice_id: int, *, reason: str | None = None
    ) -> MocoResponse[None]:
        """Delete an invoice."""
        if reason is not None:
            return self._transport.request(
                "DELETE",
                f"/invoices/{invoice_id}",
                json_data={"reason": reason},
                cast_to=None,
            )
        return self._delete(f"/invoices/{invoice_id}")

    def list_attachments(self, invoice_id: int) -> SyncPage[dict[str, Any]]:
        """List all attachments for an invoice."""
        return self._get_list(
            f"/invoices/{invoice_id}/attachments",
            cast_to=dict,
        )

    def create_attachment(
        self,
        invoice_id: int,
        *,
        filename: str,
        base64: str,
    ) -> MocoResponse[None]:
        """Add an attachment PDF to an invoice."""
        return self._post(
            f"/invoices/{invoice_id}/attachments",
            json_data={"attachment": {"filename": filename, "base64": base64}},
            cast_to=None,  # type: ignore[arg-type]
        )

    def delete_attachment(
        self, invoice_id: int, attachment_id: int
    ) -> MocoResponse[None]:
        """Remove an attachment from an invoice."""
        return self._delete(f"/invoices/{invoice_id}/attachments/{attachment_id}")


class AsyncInvoices(AsyncResource):
    """Asynchronous invoices resource."""

    async def list(
        self,
        *,
        status: InvoiceStatus | None = None,
        include_disregarded: bool | None = None,
        not_booked: bool | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        tags: str | None = None,
        identifier: str | None = None,
        term: str | None = None,
        company_id: int | None = None,
        project_id: int | None = None,
    ) -> AsyncPage[Invoice]:
        """Retrieve all invoices."""
        params = _filter_params(
            status=status,
            include_disregarded=include_disregarded,
            not_booked=not_booked,
            date_from=date_from,
            date_to=date_to,
            service_period_from=service_period_from,
            service_period_to=service_period_to,
            tags=tags,
            identifier=identifier,
            term=term,
            company_id=company_id,
            project_id=project_id,
        )
        return await self._get_list("/invoices", params=params, cast_to=Invoice)

    async def locked(
        self,
        *,
        status: InvoiceStatus | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        identifier: str | None = None,
    ) -> AsyncPage[Invoice]:
        """Retrieve all locked invoices."""
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status
        if date_from is not None:
            params["date_from"] = date_from
        if date_to is not None:
            params["date_to"] = date_to
        if identifier is not None:
            params["identifier"] = identifier
        return await self._get_list(
            "/invoices/locked",
            params=params or None,
            cast_to=Invoice,
        )

    async def get(self, invoice_id: int) -> MocoResponse[Invoice]:
        """Retrieve a single invoice."""
        return await self._get(f"/invoices/{invoice_id}", cast_to=Invoice)

    async def create(
        self,
        *,
        customer_id: int,
        recipient_address: str,
        date: str,
        due_date: str,
        title: str,
        tax: float,
        currency: str,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        status: InvoiceStatus | None = None,
        project_id: int | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        change_address: InvoiceChangeAddress | None = None,
        salutation: str | None = None,
        footer: str | None = None,
        discount: float | None = None,
        cash_discount: float | None = None,
        cash_discount_days: int | None = None,
        internal_contact_id: int | None = None,
        custom_properties: dict[str, str] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
        print_detail_columns: bool | None = None,
    ) -> MocoResponse[Invoice]:
        """Create an invoice."""
        data: dict[str, Any] = {
            "customer_id": customer_id,
            "recipient_address": recipient_address,
            "date": date,
            "due_date": due_date,
            "title": title,
            "tax": tax,
            "currency": currency,
            "items": items,
        }
        if status is not None:
            data["status"] = status
        if project_id is not None:
            data["project_id"] = project_id
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if change_address is not None:
            data["change_address"] = change_address
        if salutation is not None:
            data["salutation"] = salutation
        if footer is not None:
            data["footer"] = footer
        if discount is not None:
            data["discount"] = discount
        if cash_discount is not None:
            data["cash_discount"] = cash_discount
        if cash_discount_days is not None:
            data["cash_discount_days"] = cash_discount_days
        if internal_contact_id is not None:
            data["internal_contact_id"] = internal_contact_id
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if tags is not None:
            data["tags"] = tags
        if print_detail_columns is not None:
            data["print_detail_columns"] = print_detail_columns
        return await self._post("/invoices", json_data=data, cast_to=Invoice)

    async def timesheet(self, invoice_id: int) -> AsyncPage[InvoiceTimesheetActivity]:
        """Retrieve the timesheet for an invoice."""
        return await self._get_list(
            f"/invoices/{invoice_id}/timesheet",
            cast_to=InvoiceTimesheetActivity,
        )

    async def expenses(self, invoice_id: int) -> AsyncPage[InvoiceExpense]:
        """Retrieve expenses for an invoice."""
        return await self._get_list(
            f"/invoices/{invoice_id}/expenses",
            cast_to=InvoiceExpense,
        )

    async def update_status(
        self, invoice_id: int, *, status: InvoiceStatus
    ) -> MocoResponse[None]:
        """Update an invoice status."""
        return await self._put(
            f"/invoices/{invoice_id}/update_status",
            json_data={"status": status},
            cast_to=None,  # type: ignore[arg-type]
        )

    async def send_email(
        self,
        invoice_id: int,
        *,
        subject: str,
        text: str,
        emails_to: str | None = None,
        emails_cc: str | None = None,
        emails_bcc: str | None = None,
        letter_paper_id: int | None = None,
    ) -> MocoResponse[None]:
        """Send the invoice by email."""
        data: dict[str, Any] = {"subject": subject, "text": text}
        if emails_to is not None:
            data["emails_to"] = emails_to
        if emails_cc is not None:
            data["emails_cc"] = emails_cc
        if emails_bcc is not None:
            data["emails_bcc"] = emails_bcc
        if letter_paper_id is not None:
            data["letter_paper_id"] = letter_paper_id
        return await self._post(
            f"/invoices/{invoice_id}/send_email",
            json_data=data,
            cast_to=None,  # type: ignore[arg-type]
        )

    async def delete(
        self, invoice_id: int, *, reason: str | None = None
    ) -> MocoResponse[None]:
        """Delete an invoice."""
        if reason is not None:
            return await self._transport.request(
                "DELETE",
                f"/invoices/{invoice_id}",
                json_data={"reason": reason},
                cast_to=None,
            )
        return await self._delete(f"/invoices/{invoice_id}")

    async def list_attachments(self, invoice_id: int) -> AsyncPage[dict[str, Any]]:
        """List all attachments for an invoice."""
        return await self._get_list(
            f"/invoices/{invoice_id}/attachments",
            cast_to=dict,
        )

    async def create_attachment(
        self,
        invoice_id: int,
        *,
        filename: str,
        base64: str,
    ) -> MocoResponse[None]:
        """Add an attachment PDF to an invoice."""
        return await self._post(
            f"/invoices/{invoice_id}/attachments",
            json_data={"attachment": {"filename": filename, "base64": base64}},
            cast_to=None,  # type: ignore[arg-type]
        )

    async def delete_attachment(
        self, invoice_id: int, attachment_id: int
    ) -> MocoResponse[None]:
        """Remove an attachment from an invoice."""
        return await self._delete(f"/invoices/{invoice_id}/attachments/{attachment_id}")
