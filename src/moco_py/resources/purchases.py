"""Purchases resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import PaymentMethod, PurchaseStatus
from ..types.purchases import Purchase


class Purchases(SyncResource):
    """Synchronous purchases resource."""

    def list(
        self,
        *,
        category_id: int | None = None,
        term: str | None = None,
        company_id: int | None = None,
        status: PurchaseStatus | None = None,
        not_booked: bool | None = None,
        tags: str | None = None,
        date: str | None = None,
        unpaid: bool | None = None,
        payment_method: PaymentMethod | None = None,
        receipt_identifier: str | None = None,
        identifier: str | None = None,
    ) -> SyncPage[Purchase]:
        """Retrieve all purchases."""
        params: dict[str, Any] = {}
        if category_id is not None:
            params["category_id"] = category_id
        if term is not None:
            params["term"] = term
        if company_id is not None:
            params["company_id"] = company_id
        if status is not None:
            params["status"] = status
        if not_booked is not None:
            params["not_booked"] = not_booked
        if tags is not None:
            params["tags"] = tags
        if date is not None:
            params["date"] = date
        if unpaid is not None:
            params["unpaid"] = unpaid
        if payment_method is not None:
            params["payment_method"] = payment_method
        if receipt_identifier is not None:
            params["receipt_identifier"] = receipt_identifier
        if identifier is not None:
            params["identifier"] = identifier
        return self._get_list("/purchases", params=params, cast_to=Purchase)

    def get(self, purchase_id: int) -> MocoResponse[Purchase]:
        """Retrieve a single purchase."""
        return self._get(f"/purchases/{purchase_id}", cast_to=Purchase)

    def create(
        self,
        *,
        date: str,
        currency: str,
        payment_method: PaymentMethod,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        title: str | None = None,
        due_date: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        status: PurchaseStatus | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        receipt_identifier: str | None = None,
        info: str | None = None,
        iban: str | None = None,
        reference: str | None = None,
        custom_property_values: dict[str, Any] | None = None,
        file: dict[str, str] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Purchase]:
        """Create a purchase."""
        body: dict[str, Any] = {
            "date": date,
            "currency": currency,
            "payment_method": payment_method,
            "items": items,
        }
        if title is not None:
            body["title"] = title
        if due_date is not None:
            body["due_date"] = due_date
        if service_period_from is not None:
            body["service_period_from"] = service_period_from
        if service_period_to is not None:
            body["service_period_to"] = service_period_to
        if status is not None:
            body["status"] = status
        if company_id is not None:
            body["company_id"] = company_id
        if user_id is not None:
            body["user_id"] = user_id
        if receipt_identifier is not None:
            body["receipt_identifier"] = receipt_identifier
        if info is not None:
            body["info"] = info
        if iban is not None:
            body["iban"] = iban
        if reference is not None:
            body["reference"] = reference
        if custom_property_values is not None:
            body["custom_property_values"] = custom_property_values
        if file is not None:
            body["file"] = file
        if tags is not None:
            body["tags"] = tags
        return self._post("/purchases", json_data=body, cast_to=Purchase)

    def update(
        self,
        purchase_id: int,
        *,
        date: str | None = None,
        currency: str | None = None,
        payment_method: PaymentMethod | None = None,
        title: str | None = None,
        due_date: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        status: PurchaseStatus | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        receipt_identifier: str | None = None,
        info: str | None = None,
        iban: str | None = None,
        reference: str | None = None,
        custom_property_values: dict[str, Any] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Purchase]:
        """Update a purchase."""
        body: dict[str, Any] = {}
        if date is not None:
            body["date"] = date
        if currency is not None:
            body["currency"] = currency
        if payment_method is not None:
            body["payment_method"] = payment_method
        if title is not None:
            body["title"] = title
        if due_date is not None:
            body["due_date"] = due_date
        if service_period_from is not None:
            body["service_period_from"] = service_period_from
        if service_period_to is not None:
            body["service_period_to"] = service_period_to
        if status is not None:
            body["status"] = status
        if company_id is not None:
            body["company_id"] = company_id
        if user_id is not None:
            body["user_id"] = user_id
        if receipt_identifier is not None:
            body["receipt_identifier"] = receipt_identifier
        if info is not None:
            body["info"] = info
        if iban is not None:
            body["iban"] = iban
        if reference is not None:
            body["reference"] = reference
        if custom_property_values is not None:
            body["custom_property_values"] = custom_property_values
        if tags is not None:
            body["tags"] = tags
        return self._put(f"/purchases/{purchase_id}", json_data=body, cast_to=Purchase)

    def assign_to_project(
        self,
        purchase_id: int,
        *,
        item_id: int,
        project_id: int,
        expense_id: int | None = None,
        notify_project_leader: bool | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        surcharge: bool | None = None,
    ) -> MocoResponse[Purchase]:
        """Assign a purchase item to a project."""
        body: dict[str, Any] = {
            "item_id": item_id,
            "project_id": project_id,
        }
        if expense_id is not None:
            body["expense_id"] = expense_id
        if notify_project_leader is not None:
            body["notify_project_leader"] = notify_project_leader
        if billable is not None:
            body["billable"] = billable
        if budget_relevant is not None:
            body["budget_relevant"] = budget_relevant
        if surcharge is not None:
            body["surcharge"] = surcharge
        return self._post(
            f"/purchases/{purchase_id}/assign_to_project",
            json_data=body,
            cast_to=Purchase,
        )

    def update_status(self, purchase_id: int, *, status: PurchaseStatus) -> MocoResponse[Purchase]:
        """Update the purchase status."""
        return self._patch(
            f"/purchases/{purchase_id}/update_status",
            json_data={"status": status},
            cast_to=Purchase,
        )

    def delete(self, purchase_id: int) -> MocoResponse[None]:
        """Delete a purchase."""
        return self._delete(f"/purchases/{purchase_id}")


class AsyncPurchases(AsyncResource):
    """Asynchronous purchases resource."""

    async def list(
        self,
        *,
        category_id: int | None = None,
        term: str | None = None,
        company_id: int | None = None,
        status: PurchaseStatus | None = None,
        not_booked: bool | None = None,
        tags: str | None = None,
        date: str | None = None,
        unpaid: bool | None = None,
        payment_method: PaymentMethod | None = None,
        receipt_identifier: str | None = None,
        identifier: str | None = None,
    ) -> AsyncPage[Purchase]:
        """Retrieve all purchases."""
        params: dict[str, Any] = {}
        if category_id is not None:
            params["category_id"] = category_id
        if term is not None:
            params["term"] = term
        if company_id is not None:
            params["company_id"] = company_id
        if status is not None:
            params["status"] = status
        if not_booked is not None:
            params["not_booked"] = not_booked
        if tags is not None:
            params["tags"] = tags
        if date is not None:
            params["date"] = date
        if unpaid is not None:
            params["unpaid"] = unpaid
        if payment_method is not None:
            params["payment_method"] = payment_method
        if receipt_identifier is not None:
            params["receipt_identifier"] = receipt_identifier
        if identifier is not None:
            params["identifier"] = identifier
        return await self._get_list("/purchases", params=params, cast_to=Purchase)

    async def get(self, purchase_id: int) -> MocoResponse[Purchase]:
        """Retrieve a single purchase."""
        return await self._get(f"/purchases/{purchase_id}", cast_to=Purchase)

    async def create(
        self,
        *,
        date: str,
        currency: str,
        payment_method: PaymentMethod,
        items: list[dict[str, Any]],  # type: ignore[valid-type]
        title: str | None = None,
        due_date: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        status: PurchaseStatus | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        receipt_identifier: str | None = None,
        info: str | None = None,
        iban: str | None = None,
        reference: str | None = None,
        custom_property_values: dict[str, Any] | None = None,
        file: dict[str, str] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Purchase]:
        """Create a purchase."""
        body: dict[str, Any] = {
            "date": date,
            "currency": currency,
            "payment_method": payment_method,
            "items": items,
        }
        if title is not None:
            body["title"] = title
        if due_date is not None:
            body["due_date"] = due_date
        if service_period_from is not None:
            body["service_period_from"] = service_period_from
        if service_period_to is not None:
            body["service_period_to"] = service_period_to
        if status is not None:
            body["status"] = status
        if company_id is not None:
            body["company_id"] = company_id
        if user_id is not None:
            body["user_id"] = user_id
        if receipt_identifier is not None:
            body["receipt_identifier"] = receipt_identifier
        if info is not None:
            body["info"] = info
        if iban is not None:
            body["iban"] = iban
        if reference is not None:
            body["reference"] = reference
        if custom_property_values is not None:
            body["custom_property_values"] = custom_property_values
        if file is not None:
            body["file"] = file
        if tags is not None:
            body["tags"] = tags
        return await self._post("/purchases", json_data=body, cast_to=Purchase)

    async def update(
        self,
        purchase_id: int,
        *,
        date: str | None = None,
        currency: str | None = None,
        payment_method: PaymentMethod | None = None,
        title: str | None = None,
        due_date: str | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        status: PurchaseStatus | None = None,
        company_id: int | None = None,
        user_id: int | None = None,
        receipt_identifier: str | None = None,
        info: str | None = None,
        iban: str | None = None,
        reference: str | None = None,
        custom_property_values: dict[str, Any] | None = None,
        tags: list[str] | None = None,  # type: ignore[valid-type]
    ) -> MocoResponse[Purchase]:
        """Update a purchase."""
        body: dict[str, Any] = {}
        if date is not None:
            body["date"] = date
        if currency is not None:
            body["currency"] = currency
        if payment_method is not None:
            body["payment_method"] = payment_method
        if title is not None:
            body["title"] = title
        if due_date is not None:
            body["due_date"] = due_date
        if service_period_from is not None:
            body["service_period_from"] = service_period_from
        if service_period_to is not None:
            body["service_period_to"] = service_period_to
        if status is not None:
            body["status"] = status
        if company_id is not None:
            body["company_id"] = company_id
        if user_id is not None:
            body["user_id"] = user_id
        if receipt_identifier is not None:
            body["receipt_identifier"] = receipt_identifier
        if info is not None:
            body["info"] = info
        if iban is not None:
            body["iban"] = iban
        if reference is not None:
            body["reference"] = reference
        if custom_property_values is not None:
            body["custom_property_values"] = custom_property_values
        if tags is not None:
            body["tags"] = tags
        return await self._put(
            f"/purchases/{purchase_id}", json_data=body, cast_to=Purchase
        )

    async def assign_to_project(
        self,
        purchase_id: int,
        *,
        item_id: int,
        project_id: int,
        expense_id: int | None = None,
        notify_project_leader: bool | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        surcharge: bool | None = None,
    ) -> MocoResponse[Purchase]:
        """Assign a purchase item to a project."""
        body: dict[str, Any] = {
            "item_id": item_id,
            "project_id": project_id,
        }
        if expense_id is not None:
            body["expense_id"] = expense_id
        if notify_project_leader is not None:
            body["notify_project_leader"] = notify_project_leader
        if billable is not None:
            body["billable"] = billable
        if budget_relevant is not None:
            body["budget_relevant"] = budget_relevant
        if surcharge is not None:
            body["surcharge"] = surcharge
        return await self._post(
            f"/purchases/{purchase_id}/assign_to_project",
            json_data=body,
            cast_to=Purchase,
        )

    async def update_status(
        self, purchase_id: int, *, status: PurchaseStatus
    ) -> MocoResponse[Purchase]:
        """Update the purchase status."""
        return await self._patch(
            f"/purchases/{purchase_id}/update_status",
            json_data={"status": status},
            cast_to=Purchase,
        )

    async def delete(self, purchase_id: int) -> MocoResponse[None]:
        """Delete a purchase."""
        return await self._delete(f"/purchases/{purchase_id}")
