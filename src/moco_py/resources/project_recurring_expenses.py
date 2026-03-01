"""Project Recurring Expenses resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.project_recurring_expenses import ProjectRecurringExpense


class ProjectRecurringExpenses(SyncResource):
    """Synchronous project recurring expenses resource."""

    def list(self, project_id: int) -> SyncPage[ProjectRecurringExpense]:
        """Retrieve all recurring expenses for a project."""
        return self._get_list(
            f"/projects/{project_id}/recurring_expenses",
            cast_to=ProjectRecurringExpense,
        )

    def list_all(
        self, *, sort_by: str | None = None
    ) -> SyncPage[ProjectRecurringExpense]:
        """Retrieve all recurring expenses across all projects."""
        params: dict[str, Any] = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        return self._get_list(
            "/recurring_expenses",
            params=params or None,
            cast_to=ProjectRecurringExpense,
        )

    def get(
        self, project_id: int, recurring_expense_id: int
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Retrieve a single recurring expense on a project."""
        return self._get(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
            cast_to=ProjectRecurringExpense,
        )

    def create(
        self,
        project_id: int,
        *,
        start_date: str,
        period: str,
        title: str,
        quantity: float,
        unit: str,
        unit_price: float,
        unit_cost: float,
        finish_date: str | None = None,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_direction: str | None = None,
        custom_properties: dict[str, Any] | None = None,
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Create a recurring expense on a project."""
        data: dict[str, Any] = {
            "start_date": start_date,
            "period": period,
            "title": title,
            "quantity": quantity,
            "unit": unit,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
        }
        if finish_date is not None:
            data["finish_date"] = finish_date
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_direction is not None:
            data["service_period_direction"] = service_period_direction
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        return self._post(
            f"/projects/{project_id}/recurring_expenses",
            json_data=data,
            cast_to=ProjectRecurringExpense,
        )

    def update(
        self,
        project_id: int,
        recurring_expense_id: int,
        *,
        title: str | None = None,
        quantity: float | None = None,
        unit: str | None = None,
        unit_price: float | None = None,
        unit_cost: float | None = None,
        finish_date: str | None = None,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_direction: str | None = None,
        custom_properties: dict[str, Any] | None = None,
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Update a recurring expense on a project."""
        data: dict[str, Any] = {}
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
        if finish_date is not None:
            data["finish_date"] = finish_date
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_direction is not None:
            data["service_period_direction"] = service_period_direction
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        return self._put(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
            json_data=data,
            cast_to=ProjectRecurringExpense,
        )

    def recur(
        self, project_id: int, recurring_expense_id: int
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Trigger creation of an additional service entry ahead of schedule."""
        return self._post(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}/recur",
            cast_to=ProjectRecurringExpense,
        )

    def delete(self, project_id: int, recurring_expense_id: int) -> MocoResponse[None]:
        """Delete a recurring expense on a project."""
        return self._delete(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}"
        )


class AsyncProjectRecurringExpenses(AsyncResource):
    """Asynchronous project recurring expenses resource."""

    async def list(self, project_id: int) -> AsyncPage[ProjectRecurringExpense]:
        """Retrieve all recurring expenses for a project."""
        return await self._get_list(
            f"/projects/{project_id}/recurring_expenses",
            cast_to=ProjectRecurringExpense,
        )

    async def list_all(
        self, *, sort_by: str | None = None
    ) -> AsyncPage[ProjectRecurringExpense]:
        """Retrieve all recurring expenses across all projects."""
        params: dict[str, Any] = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        return await self._get_list(
            "/recurring_expenses",
            params=params or None,
            cast_to=ProjectRecurringExpense,
        )

    async def get(
        self, project_id: int, recurring_expense_id: int
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Retrieve a single recurring expense on a project."""
        return await self._get(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
            cast_to=ProjectRecurringExpense,
        )

    async def create(
        self,
        project_id: int,
        *,
        start_date: str,
        period: str,
        title: str,
        quantity: float,
        unit: str,
        unit_price: float,
        unit_cost: float,
        finish_date: str | None = None,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_direction: str | None = None,
        custom_properties: dict[str, Any] | None = None,
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Create a recurring expense on a project."""
        data: dict[str, Any] = {
            "start_date": start_date,
            "period": period,
            "title": title,
            "quantity": quantity,
            "unit": unit,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
        }
        if finish_date is not None:
            data["finish_date"] = finish_date
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_direction is not None:
            data["service_period_direction"] = service_period_direction
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        return await self._post(
            f"/projects/{project_id}/recurring_expenses",
            json_data=data,
            cast_to=ProjectRecurringExpense,
        )

    async def update(
        self,
        project_id: int,
        recurring_expense_id: int,
        *,
        title: str | None = None,
        quantity: float | None = None,
        unit: str | None = None,
        unit_price: float | None = None,
        unit_cost: float | None = None,
        finish_date: str | None = None,
        description: str | None = None,
        billable: bool | None = None,
        budget_relevant: bool | None = None,
        service_period_direction: str | None = None,
        custom_properties: dict[str, Any] | None = None,
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Update a recurring expense on a project."""
        data: dict[str, Any] = {}
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
        if finish_date is not None:
            data["finish_date"] = finish_date
        if description is not None:
            data["description"] = description
        if billable is not None:
            data["billable"] = billable
        if budget_relevant is not None:
            data["budget_relevant"] = budget_relevant
        if service_period_direction is not None:
            data["service_period_direction"] = service_period_direction
        if custom_properties is not None:
            data["custom_properties"] = custom_properties
        return await self._put(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
            json_data=data,
            cast_to=ProjectRecurringExpense,
        )

    async def recur(
        self, project_id: int, recurring_expense_id: int
    ) -> MocoResponse[ProjectRecurringExpense]:
        """Trigger creation of an additional service entry ahead of schedule."""
        return await self._post(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}/recur",
            cast_to=ProjectRecurringExpense,
        )

    async def delete(
        self, project_id: int, recurring_expense_id: int
    ) -> MocoResponse[None]:
        """Delete a recurring expense on a project."""
        return await self._delete(
            f"/projects/{project_id}/recurring_expenses/{recurring_expense_id}"
        )
