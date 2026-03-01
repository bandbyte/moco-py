"""Invoice Bookkeeping Exports resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.invoice_bookkeeping_exports import InvoiceBookkeepingExport


class InvoiceBookkeepingExports(SyncResource):
    """Synchronous invoice bookkeeping exports resource."""

    def list(self) -> SyncPage[InvoiceBookkeepingExport]:
        """Retrieve all invoice bookkeeping exports."""
        return self._get_list(
            "/invoices/bookkeeping_exports",
            cast_to=InvoiceBookkeepingExport,
        )

    def get(self, export_id: int) -> MocoResponse[InvoiceBookkeepingExport]:
        """Retrieve a single invoice bookkeeping export."""
        return self._get(
            f"/invoices/bookkeeping_exports/{export_id}",
            cast_to=InvoiceBookkeepingExport,
        )

    def create(
        self,
        *,
        invoice_ids: list[int],  # type: ignore[valid-type]
        trigger_submission: bool | None = None,
        comment: str | None = None,
    ) -> MocoResponse[InvoiceBookkeepingExport]:
        """Create an invoice bookkeeping export."""
        data: dict[str, Any] = {"invoice_ids": invoice_ids}
        if trigger_submission is not None:
            data["trigger_submission"] = trigger_submission
        if comment is not None:
            data["comment"] = comment
        return self._post(
            "/invoices/bookkeeping_exports",
            json_data=data,
            cast_to=InvoiceBookkeepingExport,
        )


class AsyncInvoiceBookkeepingExports(AsyncResource):
    """Asynchronous invoice bookkeeping exports resource."""

    async def list(self) -> AsyncPage[InvoiceBookkeepingExport]:
        """Retrieve all invoice bookkeeping exports."""
        return await self._get_list(
            "/invoices/bookkeeping_exports",
            cast_to=InvoiceBookkeepingExport,
        )

    async def get(self, export_id: int) -> MocoResponse[InvoiceBookkeepingExport]:
        """Retrieve a single invoice bookkeeping export."""
        return await self._get(
            f"/invoices/bookkeeping_exports/{export_id}",
            cast_to=InvoiceBookkeepingExport,
        )

    async def create(
        self,
        *,
        invoice_ids: list[int],  # type: ignore[valid-type]
        trigger_submission: bool | None = None,
        comment: str | None = None,
    ) -> MocoResponse[InvoiceBookkeepingExport]:
        """Create an invoice bookkeeping export."""
        data: dict[str, Any] = {"invoice_ids": invoice_ids}
        if trigger_submission is not None:
            data["trigger_submission"] = trigger_submission
        if comment is not None:
            data["comment"] = comment
        return await self._post(
            "/invoices/bookkeeping_exports",
            json_data=data,
            cast_to=InvoiceBookkeepingExport,
        )
