"""Purchase Bookkeeping Exports resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.purchase_bookkeeping_exports import PurchaseBookkeepingExport


class PurchaseBookkeepingExports(SyncResource):
    """Synchronous purchase bookkeeping exports resource."""

    def list(self) -> SyncPage[PurchaseBookkeepingExport]:
        """Retrieve all purchase bookkeeping exports."""
        return self._get_list(
            "/purchases/bookkeeping_exports",
            cast_to=PurchaseBookkeepingExport,
        )

    def get(self, export_id: int) -> MocoResponse[PurchaseBookkeepingExport]:
        """Retrieve a single purchase bookkeeping export."""
        return self._get(
            f"/purchases/bookkeeping_exports/{export_id}",
            cast_to=PurchaseBookkeepingExport,
        )

    def create(
        self,
        *,
        purchase_ids: list[int],  # type: ignore[valid-type]
        trigger_submission: bool | None = None,
        archive_after_export: bool | None = None,
        comment: str | None = None,
    ) -> MocoResponse[PurchaseBookkeepingExport]:
        """Create a purchase bookkeeping export."""
        data: dict[str, Any] = {"purchase_ids": purchase_ids}
        if trigger_submission is not None:
            data["trigger_submission"] = trigger_submission
        if archive_after_export is not None:
            data["archive_after_export"] = archive_after_export
        if comment is not None:
            data["comment"] = comment
        return self._post(
            "/purchases/bookkeeping_exports",
            json_data=data,
            cast_to=PurchaseBookkeepingExport,
        )


class AsyncPurchaseBookkeepingExports(AsyncResource):
    """Asynchronous purchase bookkeeping exports resource."""

    async def list(self) -> AsyncPage[PurchaseBookkeepingExport]:
        """Retrieve all purchase bookkeeping exports."""
        return await self._get_list(
            "/purchases/bookkeeping_exports",
            cast_to=PurchaseBookkeepingExport,
        )

    async def get(self, export_id: int) -> MocoResponse[PurchaseBookkeepingExport]:
        """Retrieve a single purchase bookkeeping export."""
        return await self._get(
            f"/purchases/bookkeeping_exports/{export_id}",
            cast_to=PurchaseBookkeepingExport,
        )

    async def create(
        self,
        *,
        purchase_ids: list[int],  # type: ignore[valid-type]
        trigger_submission: bool | None = None,
        archive_after_export: bool | None = None,
        comment: str | None = None,
    ) -> MocoResponse[PurchaseBookkeepingExport]:
        """Create a purchase bookkeeping export."""
        data: dict[str, Any] = {"purchase_ids": purchase_ids}
        if trigger_submission is not None:
            data["trigger_submission"] = trigger_submission
        if archive_after_export is not None:
            data["archive_after_export"] = archive_after_export
        if comment is not None:
            data["comment"] = comment
        return await self._post(
            "/purchases/bookkeeping_exports",
            json_data=data,
            cast_to=PurchaseBookkeepingExport,
        )
