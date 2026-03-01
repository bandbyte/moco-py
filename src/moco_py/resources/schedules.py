"""Schedules (Absences) resource."""

from __future__ import annotations

from typing import Any

from .._pagination import AsyncPage, SyncPage
from .._resource import AsyncResource, SyncResource
from .._response import MocoResponse
from ..types._enums import AbsenceCode, ScheduleSymbol
from ..types.schedules import Schedule


class Schedules(SyncResource):
    """Synchronous schedules resource."""

    def list(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        user_id: int | None = None,
        absence_code: AbsenceCode | None = None,
        holiday_request_id: int | None = None,
    ) -> SyncPage[Schedule]:
        """Retrieve all schedule entries."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if user_id is not None:
            params["user_id"] = user_id
        if absence_code is not None:
            params["absence_code"] = absence_code
        if holiday_request_id is not None:
            params["holiday_request_id"] = holiday_request_id
        return self._get_list("/schedules", params=params or None, cast_to=Schedule)

    def get(self, schedule_id: int) -> MocoResponse[Schedule]:
        """Retrieve a single schedule entry."""
        return self._get(f"/schedules/{schedule_id}", cast_to=Schedule)

    def create(
        self,
        *,
        date: str,
        absence_code: AbsenceCode,
        user_id: int | None = None,
        am: bool | None = None,
        pm: bool | None = None,
        comment: str | None = None,
        symbol: ScheduleSymbol | None = None,
        overwrite: bool | None = None,
    ) -> MocoResponse[Schedule]:
        """Create a schedule entry."""
        body: dict[str, Any] = {"date": date, "absence_code": absence_code}
        if user_id is not None:
            body["user_id"] = user_id
        if am is not None:
            body["am"] = am
        if pm is not None:
            body["pm"] = pm
        if comment is not None:
            body["comment"] = comment
        if symbol is not None:
            body["symbol"] = symbol
        if overwrite is not None:
            body["overwrite"] = overwrite
        return self._post("/schedules", json_data=body, cast_to=Schedule)

    def update(
        self,
        schedule_id: int,
        *,
        date: str | None = None,
        absence_code: AbsenceCode | None = None,
        user_id: int | None = None,
        am: bool | None = None,
        pm: bool | None = None,
        comment: str | None = None,
        symbol: ScheduleSymbol | None = None,
        overwrite: bool | None = None,
    ) -> MocoResponse[Schedule]:
        """Update a schedule entry."""
        body: dict[str, Any] = {}
        if date is not None:
            body["date"] = date
        if absence_code is not None:
            body["absence_code"] = absence_code
        if user_id is not None:
            body["user_id"] = user_id
        if am is not None:
            body["am"] = am
        if pm is not None:
            body["pm"] = pm
        if comment is not None:
            body["comment"] = comment
        if symbol is not None:
            body["symbol"] = symbol
        if overwrite is not None:
            body["overwrite"] = overwrite
        return self._put(f"/schedules/{schedule_id}", json_data=body, cast_to=Schedule)

    def delete(self, schedule_id: int) -> MocoResponse[None]:
        """Delete a schedule entry."""
        return self._delete(f"/schedules/{schedule_id}")


class AsyncSchedules(AsyncResource):
    """Asynchronous schedules resource."""

    async def list(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
        user_id: int | None = None,
        absence_code: AbsenceCode | None = None,
        holiday_request_id: int | None = None,
    ) -> AsyncPage[Schedule]:
        """Retrieve all schedule entries."""
        params: dict[str, Any] = {}
        if from_date is not None:
            params["from"] = from_date
        if to_date is not None:
            params["to"] = to_date
        if user_id is not None:
            params["user_id"] = user_id
        if absence_code is not None:
            params["absence_code"] = absence_code
        if holiday_request_id is not None:
            params["holiday_request_id"] = holiday_request_id
        return await self._get_list(
            "/schedules", params=params or None, cast_to=Schedule
        )

    async def get(self, schedule_id: int) -> MocoResponse[Schedule]:
        """Retrieve a single schedule entry."""
        return await self._get(f"/schedules/{schedule_id}", cast_to=Schedule)

    async def create(
        self,
        *,
        date: str,
        absence_code: AbsenceCode,
        user_id: int | None = None,
        am: bool | None = None,
        pm: bool | None = None,
        comment: str | None = None,
        symbol: ScheduleSymbol | None = None,
        overwrite: bool | None = None,
    ) -> MocoResponse[Schedule]:
        """Create a schedule entry."""
        body: dict[str, Any] = {"date": date, "absence_code": absence_code}
        if user_id is not None:
            body["user_id"] = user_id
        if am is not None:
            body["am"] = am
        if pm is not None:
            body["pm"] = pm
        if comment is not None:
            body["comment"] = comment
        if symbol is not None:
            body["symbol"] = symbol
        if overwrite is not None:
            body["overwrite"] = overwrite
        return await self._post("/schedules", json_data=body, cast_to=Schedule)

    async def update(
        self,
        schedule_id: int,
        *,
        date: str | None = None,
        absence_code: AbsenceCode | None = None,
        user_id: int | None = None,
        am: bool | None = None,
        pm: bool | None = None,
        comment: str | None = None,
        symbol: ScheduleSymbol | None = None,
        overwrite: bool | None = None,
    ) -> MocoResponse[Schedule]:
        """Update a schedule entry."""
        body: dict[str, Any] = {}
        if date is not None:
            body["date"] = date
        if absence_code is not None:
            body["absence_code"] = absence_code
        if user_id is not None:
            body["user_id"] = user_id
        if am is not None:
            body["am"] = am
        if pm is not None:
            body["pm"] = pm
        if comment is not None:
            body["comment"] = comment
        if symbol is not None:
            body["symbol"] = symbol
        if overwrite is not None:
            body["overwrite"] = overwrite
        return await self._put(
            f"/schedules/{schedule_id}", json_data=body, cast_to=Schedule
        )

    async def delete(self, schedule_id: int) -> MocoResponse[None]:
        """Delete a schedule entry."""
        return await self._delete(f"/schedules/{schedule_id}")
