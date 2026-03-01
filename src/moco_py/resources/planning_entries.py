"""Planning Entries resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import PlanningSymbol
from ..types.planning_entries import PlanningEntry


class PlanningEntries(SyncResource):
    """Synchronous planning entries resource."""

    def list(
        self,
        *,
        period: str | None = None,
        user_id: int | None = None,
        project_id: int | None = None,
        deal_id: int | None = None,
    ) -> SyncPage[PlanningEntry]:
        """Retrieve all planning entries."""
        params: dict[str, Any] = {}
        if period is not None:
            params["period"] = period
        if user_id is not None:
            params["user_id"] = user_id
        if project_id is not None:
            params["project_id"] = project_id
        if deal_id is not None:
            params["deal_id"] = deal_id
        return self._get_list(
            "/planning_entries", params=params or None, cast_to=PlanningEntry
        )

    def get(self, entry_id: int) -> MocoResponse[PlanningEntry]:
        """Retrieve a single planning entry."""
        return self._get(f"/planning_entries/{entry_id}", cast_to=PlanningEntry)

    def create(
        self,
        *,
        starts_on: str,
        ends_on: str,
        hours_per_day: float,
        project_id: int | None = None,
        deal_id: int | None = None,
        user_id: int | None = None,
        task_id: int | None = None,
        comment: str | None = None,
        symbol: PlanningSymbol | None = None,
        tentative: bool | None = None,
    ) -> MocoResponse[PlanningEntry]:
        """Create a planning entry."""
        data: dict[str, Any] = {
            "starts_on": starts_on,
            "ends_on": ends_on,
            "hours_per_day": hours_per_day,
        }
        if project_id is not None:
            data["project_id"] = project_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if user_id is not None:
            data["user_id"] = user_id
        if task_id is not None:
            data["task_id"] = task_id
        if comment is not None:
            data["comment"] = comment
        if symbol is not None:
            data["symbol"] = symbol
        if tentative is not None:
            data["tentative"] = tentative
        return self._post("/planning_entries", json_data=data, cast_to=PlanningEntry)

    def update(
        self,
        entry_id: int,
        *,
        starts_on: str | None = None,
        ends_on: str | None = None,
        hours_per_day: float | None = None,
        project_id: int | None = None,
        deal_id: int | None = None,
        user_id: int | None = None,
        task_id: int | None = None,
        comment: str | None = None,
        symbol: PlanningSymbol | None = None,
        tentative: bool | None = None,
    ) -> MocoResponse[PlanningEntry]:
        """Update a planning entry."""
        data: dict[str, Any] = {}
        if starts_on is not None:
            data["starts_on"] = starts_on
        if ends_on is not None:
            data["ends_on"] = ends_on
        if hours_per_day is not None:
            data["hours_per_day"] = hours_per_day
        if project_id is not None:
            data["project_id"] = project_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if user_id is not None:
            data["user_id"] = user_id
        if task_id is not None:
            data["task_id"] = task_id
        if comment is not None:
            data["comment"] = comment
        if symbol is not None:
            data["symbol"] = symbol
        if tentative is not None:
            data["tentative"] = tentative
        return self._put(
            f"/planning_entries/{entry_id}",
            json_data=data,
            cast_to=PlanningEntry,
        )

    def delete(self, entry_id: int) -> MocoResponse[None]:
        """Delete a planning entry."""
        return self._delete(f"/planning_entries/{entry_id}")


class AsyncPlanningEntries(AsyncResource):
    """Asynchronous planning entries resource."""

    async def list(
        self,
        *,
        period: str | None = None,
        user_id: int | None = None,
        project_id: int | None = None,
        deal_id: int | None = None,
    ) -> AsyncPage[PlanningEntry]:
        """Retrieve all planning entries."""
        params: dict[str, Any] = {}
        if period is not None:
            params["period"] = period
        if user_id is not None:
            params["user_id"] = user_id
        if project_id is not None:
            params["project_id"] = project_id
        if deal_id is not None:
            params["deal_id"] = deal_id
        return await self._get_list(
            "/planning_entries", params=params or None, cast_to=PlanningEntry
        )

    async def get(self, entry_id: int) -> MocoResponse[PlanningEntry]:
        """Retrieve a single planning entry."""
        return await self._get(f"/planning_entries/{entry_id}", cast_to=PlanningEntry)

    async def create(
        self,
        *,
        starts_on: str,
        ends_on: str,
        hours_per_day: float,
        project_id: int | None = None,
        deal_id: int | None = None,
        user_id: int | None = None,
        task_id: int | None = None,
        comment: str | None = None,
        symbol: PlanningSymbol | None = None,
        tentative: bool | None = None,
    ) -> MocoResponse[PlanningEntry]:
        """Create a planning entry."""
        data: dict[str, Any] = {
            "starts_on": starts_on,
            "ends_on": ends_on,
            "hours_per_day": hours_per_day,
        }
        if project_id is not None:
            data["project_id"] = project_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if user_id is not None:
            data["user_id"] = user_id
        if task_id is not None:
            data["task_id"] = task_id
        if comment is not None:
            data["comment"] = comment
        if symbol is not None:
            data["symbol"] = symbol
        if tentative is not None:
            data["tentative"] = tentative
        return await self._post(
            "/planning_entries", json_data=data, cast_to=PlanningEntry
        )

    async def update(
        self,
        entry_id: int,
        *,
        starts_on: str | None = None,
        ends_on: str | None = None,
        hours_per_day: float | None = None,
        project_id: int | None = None,
        deal_id: int | None = None,
        user_id: int | None = None,
        task_id: int | None = None,
        comment: str | None = None,
        symbol: PlanningSymbol | None = None,
        tentative: bool | None = None,
    ) -> MocoResponse[PlanningEntry]:
        """Update a planning entry."""
        data: dict[str, Any] = {}
        if starts_on is not None:
            data["starts_on"] = starts_on
        if ends_on is not None:
            data["ends_on"] = ends_on
        if hours_per_day is not None:
            data["hours_per_day"] = hours_per_day
        if project_id is not None:
            data["project_id"] = project_id
        if deal_id is not None:
            data["deal_id"] = deal_id
        if user_id is not None:
            data["user_id"] = user_id
        if task_id is not None:
            data["task_id"] = task_id
        if comment is not None:
            data["comment"] = comment
        if symbol is not None:
            data["symbol"] = symbol
        if tentative is not None:
            data["tentative"] = tentative
        return await self._put(
            f"/planning_entries/{entry_id}",
            json_data=data,
            cast_to=PlanningEntry,
        )

    async def delete(self, entry_id: int) -> MocoResponse[None]:
        """Delete a planning entry."""
        return await self._delete(f"/planning_entries/{entry_id}")
