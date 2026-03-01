"""Purchase Payments resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.purchase_payments import PurchasePayment


class PurchasePayments(SyncResource):
    """Synchronous purchase payments resource."""

    def list(
        self,
        *,
        purchase_id: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> SyncPage[PurchasePayment]:
        """Retrieve all purchase payments."""
        params: dict[str, Any] = {}
        if purchase_id is not None:
            params["purchase_id"] = purchase_id
        if date_from is not None:
            params["date_from"] = date_from
        if date_to is not None:
            params["date_to"] = date_to
        return self._get_list(
            "/purchases/payments", params=params, cast_to=PurchasePayment
        )

    def get(self, payment_id: int) -> MocoResponse[PurchasePayment]:
        """Retrieve a single purchase payment."""
        return self._get(f"/purchases/payments/{payment_id}", cast_to=PurchasePayment)

    def create(
        self,
        *,
        date: str,
        total: float,
        purchase_id: int | None = None,
        description: str | None = None,
    ) -> MocoResponse[PurchasePayment]:
        """Create a purchase payment."""
        body: dict[str, Any] = {"date": date, "total": total}
        if purchase_id is not None:
            body["purchase_id"] = purchase_id
        if description is not None:
            body["description"] = description
        return self._post(
            "/purchases/payments", json_data=body, cast_to=PurchasePayment
        )

    def create_bulk(
        self,
        *,
        bulk_data: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[list[PurchasePayment]]:  # type: ignore[valid-type]
        """Create multiple purchase payments in bulk."""
        return self._post(
            "/purchases/payments/bulk",
            json_data={"bulk_data": bulk_data},
            cast_to=PurchasePayment,
        )

    def update(
        self,
        payment_id: int,
        *,
        date: str | None = None,
        total: float | None = None,
        description: str | None = None,
    ) -> MocoResponse[PurchasePayment]:
        """Update a purchase payment."""
        body: dict[str, Any] = {}
        if date is not None:
            body["date"] = date
        if total is not None:
            body["total"] = total
        if description is not None:
            body["description"] = description
        return self._put(
            f"/purchases/payments/{payment_id}",
            json_data=body,
            cast_to=PurchasePayment,
        )

    def delete(self, payment_id: int) -> MocoResponse[None]:
        """Delete a purchase payment."""
        return self._delete(f"/purchases/payments/{payment_id}")


class AsyncPurchasePayments(AsyncResource):
    """Asynchronous purchase payments resource."""

    async def list(
        self,
        *,
        purchase_id: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> AsyncPage[PurchasePayment]:
        """Retrieve all purchase payments."""
        params: dict[str, Any] = {}
        if purchase_id is not None:
            params["purchase_id"] = purchase_id
        if date_from is not None:
            params["date_from"] = date_from
        if date_to is not None:
            params["date_to"] = date_to
        return await self._get_list(
            "/purchases/payments", params=params, cast_to=PurchasePayment
        )

    async def get(self, payment_id: int) -> MocoResponse[PurchasePayment]:
        """Retrieve a single purchase payment."""
        return await self._get(
            f"/purchases/payments/{payment_id}", cast_to=PurchasePayment
        )

    async def create(
        self,
        *,
        date: str,
        total: float,
        purchase_id: int | None = None,
        description: str | None = None,
    ) -> MocoResponse[PurchasePayment]:
        """Create a purchase payment."""
        body: dict[str, Any] = {"date": date, "total": total}
        if purchase_id is not None:
            body["purchase_id"] = purchase_id
        if description is not None:
            body["description"] = description
        return await self._post(
            "/purchases/payments", json_data=body, cast_to=PurchasePayment
        )

    async def create_bulk(
        self,
        *,
        bulk_data: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[list[PurchasePayment]]:  # type: ignore[valid-type]
        """Create multiple purchase payments in bulk."""
        return await self._post(
            "/purchases/payments/bulk",
            json_data={"bulk_data": bulk_data},
            cast_to=PurchasePayment,
        )

    async def update(
        self,
        payment_id: int,
        *,
        date: str | None = None,
        total: float | None = None,
        description: str | None = None,
    ) -> MocoResponse[PurchasePayment]:
        """Update a purchase payment."""
        body: dict[str, Any] = {}
        if date is not None:
            body["date"] = date
        if total is not None:
            body["total"] = total
        if description is not None:
            body["description"] = description
        return await self._put(
            f"/purchases/payments/{payment_id}",
            json_data=body,
            cast_to=PurchasePayment,
        )

    async def delete(self, payment_id: int) -> MocoResponse[None]:
        """Delete a purchase payment."""
        return await self._delete(f"/purchases/payments/{payment_id}")
