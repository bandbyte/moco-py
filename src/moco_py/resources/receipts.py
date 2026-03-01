"""Receipts resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.receipts import Receipt


class Receipts(SyncResource):
    """Synchronous receipts resource."""

    def list(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        project_id: int | None = None,
        user_id: int | None = None,
        purchase_category_id: int | None = None,
        refund_request_id: str | None = None,
        submitted: bool | None = None,
    ) -> SyncPage[Receipt]:
        """Retrieve all receipts."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if project_id is not None:
            params["project_id"] = project_id
        if user_id is not None:
            params["user_id"] = user_id
        if purchase_category_id is not None:
            params["purchase_category_id"] = purchase_category_id
        if refund_request_id is not None:
            params["refund_request_id"] = refund_request_id
        if submitted is not None:
            params["submitted"] = submitted
        return self._get_list("/receipts", params=params or None, cast_to=Receipt)

    def get(self, receipt_id: int) -> MocoResponse[Receipt]:
        """Retrieve a single receipt."""
        return self._get(f"/receipts/{receipt_id}", cast_to=Receipt)

    def create(
        self,
        *,
        date: str,
        title: str,
        currency: str,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        project_id: int | None = None,
        info: str | None = None,
        billable: bool | None = None,
        attachment: dict[str, str] | None = None,
    ) -> MocoResponse[Receipt]:
        """Create a receipt."""
        data: dict[str, Any] = {
            "date": date,
            "title": title,
            "currency": currency,
            "items": items,
        }
        if project_id is not None:
            data["project_id"] = project_id
        if info is not None:
            data["info"] = info
        if billable is not None:
            data["billable"] = billable
        if attachment is not None:
            data["attachment"] = attachment
        return self._post("/receipts", json_data=data, cast_to=Receipt)

    def update(
        self,
        receipt_id: int,
        *,
        date: str | None = None,
        title: str | None = None,
        currency: str | None = None,
        items: list[dict[str, Any]] | None = None,  # type: ignore[valid-type]
        project_id: int | None = None,
        info: str | None = None,
        billable: bool | None = None,
        attachment: dict[str, str] | None = None,
    ) -> MocoResponse[Receipt]:
        """Update a receipt."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if title is not None:
            data["title"] = title
        if currency is not None:
            data["currency"] = currency
        if items is not None:
            data["items"] = items
        if project_id is not None:
            data["project_id"] = project_id
        if info is not None:
            data["info"] = info
        if billable is not None:
            data["billable"] = billable
        if attachment is not None:
            data["attachment"] = attachment
        return self._patch(f"/receipts/{receipt_id}", json_data=data, cast_to=Receipt)

    def delete(self, receipt_id: int) -> MocoResponse[None]:
        """Delete a receipt."""
        return self._delete(f"/receipts/{receipt_id}")


class AsyncReceipts(AsyncResource):
    """Asynchronous receipts resource."""

    async def list(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        project_id: int | None = None,
        user_id: int | None = None,
        purchase_category_id: int | None = None,
        refund_request_id: str | None = None,
        submitted: bool | None = None,
    ) -> AsyncPage[Receipt]:
        """Retrieve all receipts."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if project_id is not None:
            params["project_id"] = project_id
        if user_id is not None:
            params["user_id"] = user_id
        if purchase_category_id is not None:
            params["purchase_category_id"] = purchase_category_id
        if refund_request_id is not None:
            params["refund_request_id"] = refund_request_id
        if submitted is not None:
            params["submitted"] = submitted
        return await self._get_list("/receipts", params=params or None, cast_to=Receipt)

    async def get(self, receipt_id: int) -> MocoResponse[Receipt]:
        """Retrieve a single receipt."""
        return await self._get(f"/receipts/{receipt_id}", cast_to=Receipt)

    async def create(
        self,
        *,
        date: str,
        title: str,
        currency: str,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        project_id: int | None = None,
        info: str | None = None,
        billable: bool | None = None,
        attachment: dict[str, str] | None = None,
    ) -> MocoResponse[Receipt]:
        """Create a receipt."""
        data: dict[str, Any] = {
            "date": date,
            "title": title,
            "currency": currency,
            "items": items,
        }
        if project_id is not None:
            data["project_id"] = project_id
        if info is not None:
            data["info"] = info
        if billable is not None:
            data["billable"] = billable
        if attachment is not None:
            data["attachment"] = attachment
        return await self._post("/receipts", json_data=data, cast_to=Receipt)

    async def update(
        self,
        receipt_id: int,
        *,
        date: str | None = None,
        title: str | None = None,
        currency: str | None = None,
        items: list[dict[str, Any]] | None = None,  # type: ignore[valid-type]
        project_id: int | None = None,
        info: str | None = None,
        billable: bool | None = None,
        attachment: dict[str, str] | None = None,
    ) -> MocoResponse[Receipt]:
        """Update a receipt."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if title is not None:
            data["title"] = title
        if currency is not None:
            data["currency"] = currency
        if items is not None:
            data["items"] = items
        if project_id is not None:
            data["project_id"] = project_id
        if info is not None:
            data["info"] = info
        if billable is not None:
            data["billable"] = billable
        if attachment is not None:
            data["attachment"] = attachment
        return await self._patch(
            f"/receipts/{receipt_id}", json_data=data, cast_to=Receipt
        )

    async def delete(self, receipt_id: int) -> MocoResponse[None]:
        """Delete a receipt."""
        return await self._delete(f"/receipts/{receipt_id}")
