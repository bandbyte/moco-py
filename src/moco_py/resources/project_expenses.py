"""Project Expenses resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.project_expenses import ProjectExpense


class ProjectExpenses(SyncResource):
    """Synchronous project expenses resource."""

    def list(
        self,
        project_id: int,
        *,
        billable: bool | None = None,
        billed: bool | None = None,
        budget_relevant: bool | None = None,
        user_id: int | None = None,
        sort_by: str | None = None,
    ) -> SyncPage[ProjectExpense]:
        """Retrieve all additional services for a project."""
        params: dict[str, Any] = {}
        if billable is not None:
            params["billable"] = billable
        if billed is not None:
            params["billed"] = billed
        if budget_relevant is not None:
            params["budget_relevant"] = budget_relevant
        if user_id is not None:
            params["user_id"] = user_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return self._get_list(
            f"/projects/{project_id}/expenses",
            params=params or None,
            cast_to=ProjectExpense,
        )

    def list_all(
        self,
        *,
        ids: str | None = None,
        updated_after: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        billable: bool | None = None,
        billed: bool | None = None,
        budget_relevant: bool | None = None,
        tags: str | None = None,
        user_id: int | None = None,
        sort_by: str | None = None,
    ) -> SyncPage[ProjectExpense]:
        """Retrieve all additional services across all projects."""
        params: dict[str, Any] = {}
        if ids is not None:
            params["ids"] = ids
        if updated_after is not None:
            params["updated_after"] = updated_after
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if billable is not None:
            params["billable"] = billable
        if billed is not None:
            params["billed"] = billed
        if budget_relevant is not None:
            params["budget_relevant"] = budget_relevant
        if tags is not None:
            params["tags"] = tags
        if user_id is not None:
            params["user_id"] = user_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return self._get_list(
            "/projects/expenses", params=params or None, cast_to=ProjectExpense
        )

    def get(self, project_id: int, expense_id: int) -> MocoResponse[ProjectExpense]:
        """Retrieve a single additional service for a project."""
        return self._get(
            f"/projects/{project_id}/expenses/{expense_id}",
            cast_to=ProjectExpense,
        )

    def create(
        self,
        project_id: int,
        *,
        date: str,
        title: str,
        quantity: float,
        unit: str,
        unit_price: float,
        unit_cost: float,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        user_id: int | None = None,
        custom_properties: dict[str, Any] | None = None,
        file: dict[str, str] | None = None,
    ) -> MocoResponse[ProjectExpense]:
        """Create an additional service entry on a project."""
        data: dict[str, Any] = {
            "date": date,
            "title": title,
            "quantity": quantity,
            "unit": unit,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
        }
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if user_id is not None:
            data["user_id"] = user_id
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if file is not None:
            data["file"] = file
        return self._post(
            f"/projects/{project_id}/expenses",
            json_data=data,
            cast_to=ProjectExpense,
        )

    def bulk(
        self,
        project_id: int,
        *,
        bulk_data: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[list[ProjectExpense]]:  # type: ignore[valid-type]
        """Create multiple additional services entries."""
        return self._transport.request(
            "POST",
            f"/projects/{project_id}/expenses/bulk",
            json_data={"bulk_data": bulk_data},
            cast_to=ProjectExpense,
            is_list=True,
        )

    def update(
        self,
        project_id: int,
        expense_id: int,
        *,
        date: str | None = None,
        title: str | None = None,
        quantity: float | None = None,
        unit: str | None = None,
        unit_price: float | None = None,
        unit_cost: float | None = None,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        user_id: int | None = None,
        custom_properties: dict[str, Any] | None = None,
        file: dict[str, str] | None = None,
    ) -> MocoResponse[ProjectExpense]:
        """Update an additional services entry on a project."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if title is not None:
            data["title"] = title
        if quantity is not None:
            data["quantity"] = quantity
        if unit is not None:
            data["unit"] = unit
        if unit_price is not None:
            data["unit_price"] = unit_price
        if unit_cost is not None:
            data["unit_cost"] = unit_cost
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if user_id is not None:
            data["user_id"] = user_id
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if file is not None:
            data["file"] = file
        return self._put(
            f"/projects/{project_id}/expenses/{expense_id}",
            json_data=data,
            cast_to=ProjectExpense,
        )

    def delete(self, project_id: int, expense_id: int) -> MocoResponse[None]:
        """Delete an additional services entry on a project."""
        return self._delete(f"/projects/{project_id}/expenses/{expense_id}")

    def disregard(
        self,
        project_id: int,
        *,
        expense_ids: list[int],  # type: ignore[valid-type]
        reason: str,
    ) -> MocoResponse[None]:
        """Mark additional services entries as already billed."""
        return self._post(
            f"/projects/{project_id}/expenses/disregard",
            json_data={"expense_ids": expense_ids, "reason": reason},
            cast_to=None,  # type: ignore[arg-type]
        )


class AsyncProjectExpenses(AsyncResource):
    """Asynchronous project expenses resource."""

    async def list(
        self,
        project_id: int,
        *,
        billable: bool | None = None,
        billed: bool | None = None,
        budget_relevant: bool | None = None,
        user_id: int | None = None,
        sort_by: str | None = None,
    ) -> AsyncPage[ProjectExpense]:
        """Retrieve all additional services for a project."""
        params: dict[str, Any] = {}
        if billable is not None:
            params["billable"] = billable
        if billed is not None:
            params["billed"] = billed
        if budget_relevant is not None:
            params["budget_relevant"] = budget_relevant
        if user_id is not None:
            params["user_id"] = user_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return await self._get_list(
            f"/projects/{project_id}/expenses",
            params=params or None,
            cast_to=ProjectExpense,
        )

    async def list_all(
        self,
        *,
        ids: str | None = None,
        updated_after: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        billable: bool | None = None,
        billed: bool | None = None,
        budget_relevant: bool | None = None,
        tags: str | None = None,
        user_id: int | None = None,
        sort_by: str | None = None,
    ) -> AsyncPage[ProjectExpense]:
        """Retrieve all additional services across all projects."""
        params: dict[str, Any] = {}
        if ids is not None:
            params["ids"] = ids
        if updated_after is not None:
            params["updated_after"] = updated_after
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if billable is not None:
            params["billable"] = billable
        if billed is not None:
            params["billed"] = billed
        if budget_relevant is not None:
            params["budget_relevant"] = budget_relevant
        if tags is not None:
            params["tags"] = tags
        if user_id is not None:
            params["user_id"] = user_id
        if sort_by is not None:
            params["sort_by"] = sort_by
        return await self._get_list(
            "/projects/expenses", params=params or None, cast_to=ProjectExpense
        )

    async def get(
        self, project_id: int, expense_id: int
    ) -> MocoResponse[ProjectExpense]:
        """Retrieve a single additional service for a project."""
        return await self._get(
            f"/projects/{project_id}/expenses/{expense_id}",
            cast_to=ProjectExpense,
        )

    async def create(
        self,
        project_id: int,
        *,
        date: str,
        title: str,
        quantity: float,
        unit: str,
        unit_price: float,
        unit_cost: float,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        user_id: int | None = None,
        custom_properties: dict[str, Any] | None = None,
        file: dict[str, str] | None = None,
    ) -> MocoResponse[ProjectExpense]:
        """Create an additional service entry on a project."""
        data: dict[str, Any] = {
            "date": date,
            "title": title,
            "quantity": quantity,
            "unit": unit,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
        }
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if user_id is not None:
            data["user_id"] = user_id
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if file is not None:
            data["file"] = file
        return await self._post(
            f"/projects/{project_id}/expenses",
            json_data=data,
            cast_to=ProjectExpense,
        )

    async def bulk(
        self,
        project_id: int,
        *,
        bulk_data: list[dict[str, Any]],  # type: ignore[valid-type]
    ) -> MocoResponse[list[ProjectExpense]]:  # type: ignore[valid-type]
        """Create multiple additional services entries."""
        return await self._transport.request(
            "POST",
            f"/projects/{project_id}/expenses/bulk",
            json_data={"bulk_data": bulk_data},
            cast_to=ProjectExpense,
            is_list=True,
        )

    async def update(
        self,
        project_id: int,
        expense_id: int,
        *,
        date: str | None = None,
        title: str | None = None,
        quantity: float | None = None,
        unit: str | None = None,
        unit_price: float | None = None,
        unit_cost: float | None = None,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_from: str | None = None,
        service_period_to: str | None = None,
        user_id: int | None = None,
        custom_properties: dict[str, Any] | None = None,
        file: dict[str, str] | None = None,
    ) -> MocoResponse[ProjectExpense]:
        """Update an additional services entry on a project."""
        data: dict[str, Any] = {}
        if date is not None:
            data["date"] = date
        if title is not None:
            data["title"] = title
        if quantity is not None:
            data["quantity"] = quantity
        if unit is not None:
            data["unit"] = unit
        if unit_price is not None:
            data["unit_price"] = unit_price
        if unit_cost is not None:
            data["unit_cost"] = unit_cost
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_from is not None:
            data["service_period_from"] = service_period_from
        if service_period_to is not None:
            data["service_period_to"] = service_period_to
        if user_id is not None:
            data["user_id"] = user_id
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        if file is not None:
            data["file"] = file
        return await self._put(
            f"/projects/{project_id}/expenses/{expense_id}",
            json_data=data,
            cast_to=ProjectExpense,
        )

    async def delete(self, project_id: int, expense_id: int) -> MocoResponse[None]:
        """Delete an additional services entry on a project."""
        return await self._delete(f"/projects/{project_id}/expenses/{expense_id}")

    async def disregard(
        self,
        project_id: int,
        *,
        expense_ids: list[int],  # type: ignore[valid-type]
        reason: str,
    ) -> MocoResponse[None]:
        """Mark additional services entries as already billed."""
        return await self._post(
            f"/projects/{project_id}/expenses/disregard",
            json_data={"expense_ids": expense_ids, "reason": reason},
            cast_to=None,  # type: ignore[arg-type]
        )
