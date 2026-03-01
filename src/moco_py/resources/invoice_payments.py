"""Invoice Payments resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.invoice_payments import InvoicePayment


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


class InvoicePayments(SyncResource):
    """Synchronous invoice payments resource."""

    def list(
        self,
        *,
        invoice_id: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> SyncPage[InvoicePayment]:
        """Retrieve all invoice payments."""
        params = _filter_params(
            invoice_id=invoice_id, date_from=date_from, date_to=date_to
        )
        return self._get_list(
            "/invoices/payments", params=params, cast_to=InvoicePayment
        )

    def get(self, payment_id: int) -> MocoResponse[InvoicePayment]:
        """Retrieve a single invoice payment."""
        return self._get(f"/invoices/payments/{payment_id}", cast_to=InvoicePayment)

    def create(
        self,
        *,
        date: str,
        paid_total: float,
        invoice_id: int | None = None,
        currency: str | None = None,
        partially_paid: bool | None = None,
        description: str | None = None,
    ) -> MocoResponse[InvoicePayment]:
        """Create an invoice payment."""
        data: dict[str, Any] = {"date": date, "paid_total": paid_total}
        if invoice_id is not None:
            data["invoice_id"] = invoice_id
        if currency is not None:
            data["currency"] = currency
        if partially_paid is not None:
            data["partially_paid"] = partially_paid
        if description is not None:
            data["description"] = description
        return self._post("/invoices/payments", json_data=data, cast_to=InvoicePayment)

    def create_bulk(self, *, bulk_data: list[dict[str, Any]]) -> MocoResponse[None]:  # type: ignore[valid-type]
        """Create multiple invoice payments in bulk."""
        return self._post(
            "/invoices/payments/bulk",
            json_data={"bulk_data": bulk_data},
            cast_to=None,  # type: ignore[arg-type]
        )

    def update(
        self,
        payment_id: int,
        *,
        date: str | None = None,
        paid_total: float | None = None,
        currency: str | None = None,
        description: str | None = None,
    ) -> MocoResponse[InvoicePayment]:
        """Update an invoice payment."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if paid_total is not None:
            data["paid_total"] = paid_total
        if currency is not None:
            data["currency"] = currency
        if description is not None:
            data["description"] = description
        return self._put(
            f"/invoices/payments/{payment_id}",
            json_data=data,
            cast_to=InvoicePayment,
        )

    def delete(self, payment_id: int) -> MocoResponse[None]:
        """Delete an invoice payment."""
        return self._delete(f"/invoices/payments/{payment_id}")


class AsyncInvoicePayments(AsyncResource):
    """Asynchronous invoice payments resource."""

    async def list(
        self,
        *,
        invoice_id: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> AsyncPage[InvoicePayment]:
        """Retrieve all invoice payments."""
        params = _filter_params(
            invoice_id=invoice_id, date_from=date_from, date_to=date_to
        )
        return await self._get_list(
            "/invoices/payments", params=params, cast_to=InvoicePayment
        )

    async def get(self, payment_id: int) -> MocoResponse[InvoicePayment]:
        """Retrieve a single invoice payment."""
        return await self._get(
            f"/invoices/payments/{payment_id}", cast_to=InvoicePayment
        )

    async def create(
        self,
        *,
        date: str,
        paid_total: float,
        invoice_id: int | None = None,
        currency: str | None = None,
        partially_paid: bool | None = None,
        description: str | None = None,
    ) -> MocoResponse[InvoicePayment]:
        """Create an invoice payment."""
        data: dict[str, Any] = {"date": date, "paid_total": paid_total}
        if invoice_id is not None:
            data["invoice_id"] = invoice_id
        if currency is not None:
            data["currency"] = currency
        if partially_paid is not None:
            data["partially_paid"] = partially_paid
        if description is not None:
            data["description"] = description
        return await self._post(
            "/invoices/payments", json_data=data, cast_to=InvoicePayment
        )

    async def create_bulk(
        self,
        *,
        bulk_data: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[None]:
        """Create multiple invoice payments in bulk."""
        return await self._post(
            "/invoices/payments/bulk",
            json_data={"bulk_data": bulk_data},
            cast_to=None,  # type: ignore[arg-type]
        )

    async def update(
        self,
        payment_id: int,
        *,
        date: str | None = None,
        paid_total: float | None = None,
        currency: str | None = None,
        description: str | None = None,
    ) -> MocoResponse[InvoicePayment]:
        """Update an invoice payment."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if paid_total is not None:
            data["paid_total"] = paid_total
        if currency is not None:
            data["currency"] = currency
        if description is not None:
            data["description"] = description
        return await self._put(
            f"/invoices/payments/{payment_id}",
            json_data=data,
            cast_to=InvoicePayment,
        )

    async def delete(self, payment_id: int) -> MocoResponse[None]:
        """Delete an invoice payment."""
        return await self._delete(f"/invoices/payments/{payment_id}")
