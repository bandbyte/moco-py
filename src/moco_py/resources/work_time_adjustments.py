"""User Work Time Adjustments resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types.work_time_adjustments import WorkTimeAdjustment


class WorkTimeAdjustments(SyncResource):
    """Synchronous work time adjustments resource."""

    def list(
        self,
        *,
        from_date: str | None = None,
        to: str | None = None,
        user_id: int | None = None,
    ) -> SyncPage[WorkTimeAdjustment]:
        """Retrieve all work time adjustments."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to is not None:
            params["to"] = to
        if user_id is not None:
            params["user_id"] = user_id
        return self._get_list(
            "/users/work_time_adjustments",
            params=params or None,
            cast_to=WorkTimeAdjustment,
        )

    def get(self, work_time_adjustment_id: int) -> MocoResponse[WorkTimeAdjustment]:
        """Retrieve a single work time adjustment."""
        return self._get(
            f"/users/work_time_adjustments/{work_time_adjustment_id}",
            cast_to=WorkTimeAdjustment,
        )

    def create(
        self,
        *,
        user_id: int,
        description: str,
        date: str,
        hours: float,
    ) -> MocoResponse[WorkTimeAdjustment]:
        """Create a work time adjustment."""
        data: dict[str, Any] = {
            "user_id": user_id,
            "description": description,
            "date": date,
            "hours": hours,
        }
        return self._post(
            "/users/work_time_adjustments",
            json_data=data,
            cast_to=WorkTimeAdjustment,
        )

    def update(
        self,
        work_time_adjustment_id: int,
        *,
        description: str | None = None,
        date: str | None = None,
        hours: float | None = None,
    ) -> MocoResponse[WorkTimeAdjustment]:
        """Update a work time adjustment."""
        data: dict[str, Any] = {}
        for key, val in {
            "description": description,
            "date": date,
            "hours": hours,
        }.items():
            if val is not None:
                data[key] = val
        return self._put(
            f"/users/work_time_adjustments/{work_time_adjustment_id}",
            json_data=data,
            cast_to=WorkTimeAdjustment,
        )

    def delete(self, work_time_adjustment_id: int) -> MocoResponse[None]:
        """Delete a work time adjustment."""
        return self._delete(f"/users/work_time_adjustments/{work_time_adjustment_id}")


class AsyncWorkTimeAdjustments(AsyncResource):
    """Asynchronous work time adjustments resource."""

    async def list(
        self,
        *,
        from_date: str | None = None,
        to: str | None = None,
        user_id: int | None = None,
    ) -> AsyncPage[WorkTimeAdjustment]:
        """Retrieve all work time adjustments."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to is not None:
            params["to"] = to
        if user_id is not None:
            params["user_id"] = user_id
        return await self._get_list(
            "/users/work_time_adjustments",
            params=params or None,
            cast_to=WorkTimeAdjustment,
        )

    async def get(
        self, work_time_adjustment_id: int
    ) -> MocoResponse[WorkTimeAdjustment]:
        """Retrieve a single work time adjustment."""
        return await self._get(
            f"/users/work_time_adjustments/{work_time_adjustment_id}",
            cast_to=WorkTimeAdjustment,
        )

    async def create(
        self,
        *,
        user_id: int,
        description: str,
        date: str,
        hours: float,
    ) -> MocoResponse[WorkTimeAdjustment]:
        """Create a work time adjustment."""
        data: dict[str, Any] = {
            "user_id": user_id,
            "description": description,
            "date": date,
            "hours": hours,
        }
        return await self._post(
            "/users/work_time_adjustments",
            json_data=data,
            cast_to=WorkTimeAdjustment,
        )

    async def update(
        self,
        work_time_adjustment_id: int,
        *,
        description: str | None = None,
        date: str | None = None,
        hours: float | None = None,
    ) -> MocoResponse[WorkTimeAdjustment]:
        """Update a work time adjustment."""
        data: dict[str, Any] = {}
        for key, val in {
            "description": description,
            "date": date,
            "hours": hours,
        }.items():
            if val is not None:
                data[key] = val
        return await self._put(
            f"/users/work_time_adjustments/{work_time_adjustment_id}",
            json_data=data,
            cast_to=WorkTimeAdjustment,
        )

    async def delete(self, work_time_adjustment_id: int) -> MocoResponse[None]:
        """Delete a work time adjustment."""
        return await self._delete(
            f"/users/work_time_adjustments/{work_time_adjustment_id}"
        )
